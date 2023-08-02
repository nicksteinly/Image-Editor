import cv2
from flask import Flask, jsonify, request, Blueprint
from EdgeDetection import edge_detection_Canny, outer_outline_detection, thickened_edges
from Recoloration import filter_by_color, filter_out_color, recolor_white_pixels
from BackgroundRemoval import remove_black_background_to_png, overlay_image_with_mask
import numpy as np

operations_bp = Blueprint('/operations', __name__)

operations_json = {
  "Edge Detection": [
    {
      "name": "Canny Edge Detection",
      "parameters": {},
      "description": "Detects and highlights edges in the image using the Canny edge detection algorithm.",
      "corresponding_function": "edge_detection_Canny"
    },
    {
      "name": "Outer Outline Detection",
      "parameters": {},
      "description": "Finds the outer outlines of objects in the image, emphasizing their contours.",
      "corresponding_function": "outer_outline_detection"
    },
    {
      "name": "Dilate Edges",
      "parameters": {
        "Iterations": "int",
        "Kernel Size": "int"
      },
      "description": "Thickens the edges in the image by applying dilation for a specified number of iterations.",
      "corresponding_function": "thickened_edges"
    }
  ],
  "Recoloration": [
    {
      "name": "Filter by Color",
      "parameters": {
        "Target Hex Color (excluding #)": "str",
        "Threshold": "int"
      },
      "description": "Keeps only the pixels close to the target color within the specified threshold, filtering the rest.",
      "corresponding_function": "filter_by_color"
    },
    {
      "name": "Filter out Color",
      "parameters": {
        "Target Hex Color (don't include #)": "str",
        "Threshold": "int"
      },
      "description": "Removes pixels close to the target color from the image within the specified threshold.",
      "corresponding_function": "filter_out_color"
    },
    {
      "name": "Recolor White Pixels",
      "parameters": {
        "Target Hex Color (excluding #)": "str"
      },
      "description": "Changes the color of white pixels in the image to the specified color.",
      "corresponding_function": "recolor_white_pixels"
    }
  ],
  "Background Removal": [
    {
      "name": "Remove Black Background",
      "parameters": {},
      "description": "Removes the black background from the image, creating a transparent PNG with only the foreground objects.",
      "corresponding_function": "remove_black_background_to_png"
    },
    {
      "name": "Overlay Image with Mask",
      "parameters": {
        "Mask Image File Path": "str"
      },
      "description": "Overlays the image with the provided mask image, combining their content in a masked manner.",
      "corresponding_function": "overlay_image_with_mask"
    }
  ]
}

@operations_bp.route('/get_operations', methods=['GET'])
def get_operations():
    return jsonify({"operations": operations_json})

@operations_bp.route('/retrieve_operation_names', methods=['GET'])
def retrieve_operations():
    operation_names = [op['name'] for op in operations_json]
    return jsonify({"names" : operation_names})

@operations_bp.route('/retrieve_operation_parameters', methods=['POST'])
def retrieve_operation_parameters():
    data = request.json
    operation_name = data.get('operationName')
    operation = next((op for op in operations_json if op['name'] == operation_name), None)
    if operation:
        parameters = operation['parameters']
        print(parameters)
        return jsonify({"parameters": parameters})
    else:
        return jsonify({"error": "Operation not found."}), 404

@operations_bp.route('/retrieve_operation_description', methods=['POST'])
def retrieve_operation_description():
    data = request.json
    operation_name = data.get('operationName')
    operation = next((op for op in operations_json if op['name'] == operation_name), None)
    if operation:
        description = operation['description']
        return jsonify({"description": description})
    else:
        return jsonify({"error": "Operation not found."}), 404
    
@operations_bp.route('/call_operations', methods=['POST'])
def call_operation():
    try:
        data = request.json
        operations = data.get('operations')
        print(operations)
        image_input = cv2.imread("/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/" + data.get('inputImage'))
        result_image_list = []
        if operations is None:
            return jsonify({"error": "No operations found."}), 404
        
        for operation in operations:
            operation_name = operation.get('name')
            operation_type = operation.get('type')
            type_entries = operations_json.get(operation_type, [])
            json_entries = [type_entry for type_entry in type_entries if type_entry['name'] == operation_name]

            if not json_entries:
                return jsonify({"error": f"Operation '{operation_name}' not found."}), 404

            json_entry = json_entries[0]
            parameters = operation.get('parameters')
            if len(parameters) != len(json_entry.get('parameters').keys()):
                return jsonify({"error": f"Invalid parameters for operation '{operation_name}'."}), 404

            # TODO: Check if parameters are of correct type

            # Assuming the corresponding_function is a string with the function name
            corresponding_function_name = json_entry.get('corresponding_function')

            # Get the actual function object by name
            corresponding_function = globals().get(corresponding_function_name)

            if corresponding_function is None or not callable(corresponding_function):
                return jsonify({"error": f"Function '{corresponding_function_name}' not found or not callable."}), 404

            # Prepare a list of parameter values to pass to the function
            param_values = []
            for param_name, _ in json_entry.get('parameters').items():
                param_value = parameters.get(param_name)
                if param_value is None:
                    return jsonify({"error": f"Missing value for parameter '{param_name}'."}), 404

                # if not isinstance(param_value, expected_param_type):
                #     return jsonify({"error": f"Parameter type mismatch for parameter '{param_name}'."}), 404
                param_values.append(param_value)

            param_values.append(image_input)
            # Call the function with the parameter values

            image_input, result_image_encoded = corresponding_function(*param_values)
            # TODO: change image_input to the result of the function if it returns something other than the modified image.

            # Append the resulting image to the list
            result_image_list.append(result_image_encoded)

        # Return the result as a JSON response
        return {'outputImages': result_image_list}

    except Exception as e:
        return jsonify({"error": "Error occurred while executing operations.", "details": str(e)}), 500
