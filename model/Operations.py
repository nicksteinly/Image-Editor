from flask import Flask, jsonify, request, Blueprint
from EdgeDetection import edge_detection_Canny, outer_outline_detection, thickened_edges
from Recoloration import filter_by_color, filter_out_color, recolor_white_pixels
from BackgroundRemoval import remove_black_background_to_png

operations_bp = Blueprint('/operations', __name__)

operations_json = [
    { 
        "type": "Edge Detection",
        "name": "Canny Edge Detection",
        "parameters": {
            "image path": "str",
        },
        "description": "This is operation 1.",
        'corresponding_function': "edge_detection_Canny"
    },
    {
        "type": "Edge Detection",
        "name": "Outer Outline Detection",
        "parameters": {
            "image path": "str"
        },
        "description": "This is operation 2.",
        'corresponding_function': "outer_outline_detection"
    },
    {
        "type": "Edge Detection",
        "name": "Thickened Edges",
        "parameters": {
            "image path": "str",
            "iterations": "int",
            "kernel size": "int"
        },
        "description": "This is operation 3.",
        'corresponding_function': "thickened_edges"
    },
    {
        "type": "Recoloration",
        "name": "Filter by Color",
        "parameters": {
            "image path": "str",
            "target hex color (don't include #))": "str",
            "threshold": "int"
        },
        "description": "This is operation 4.",
        'corresponding_function': "filter_by_color"
    },
    {
        "type": "Recoloration",
        "name": "Filter out Color",
        "parameters": {
            "image path": "str",
            "target hex color (don't include #))": "str",
            "threshold": "int"
        },
        "description": "This is operation 5.",
        'corresponding_function': "filter_out_color"
    },
    {
        "type": "Recoloration",
        "name": "Recolor White Pixels",
        "parameters": {
            "image path": "str",
            "target hex color (don't include #))": "str"
        },
        "description": "This is operation 6.",
        'corresponding_function': "recolor_white_pixels"
    },
    {
        "type": "Background Removal",
        "name": "Remove Background",
        "parameters": {
            "image path": "str"
        },
        "description": "This is operation 7.",
        'corresponding_function': "remove_black_background_to_png"
    }
  ]

operation_names = [op['name'] for op in operations_json]

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
    #try:
        data = request.json
        operations = data.get('operations')
        if operations is None:
            return jsonify({"error": "No operations found."}), 404
        
        for operation in operations:
            print(operation)
            if operation['name'] in operation_names is None :
                return jsonify({"error": f"Operation '{operation}' not found."}), 404

            json_entry = [entry for entry in operations_json if entry['name'] == operation['name']]
            parameters = operation.get('parameters')
            if len(parameters) != len(json_entry[0].get('parameters').keys()):
                return jsonify({"error": f"Invalid parameters for operation '{operation}'."}), 404

            # TODO: Check if parameters are of correct type

            # Assuming the corresponding_function is a string with the function name
            corresponding_function_name = json_entry[0].get('corresponding_function')

            # Get the actual function object by name
            corresponding_function = globals().get(corresponding_function_name)

            if corresponding_function is None or not callable(corresponding_function):
                return jsonify({"error": f"Function '{corresponding_function_name}' not found or not callable."}), 404

            # Prepare a list of parameter values to pass to the function
            param_values = []
            for param_name, expected_param_type in parameters.items():
                param_value = operation.get('parameters').get(param_name)
                if param_value is None:
                    return jsonify({"error": f"Missing value for parameter '{param_name}'."}), 404

                # if not isinstance(param_value, expected_param_type):
                #     return jsonify({"error": f"Parameter type mismatch for parameter '{param_name}'."}), 404
                param_values.append(param_value)

            # Call the function with the parameter values
            result_image_json = corresponding_function(*param_values)

            # Return the result as a JSON response
            return result_image_json

    # except Exception as e:
    #     return jsonify({"error": "Error occurred while executing operations.", "details": str(e)}), 500
    
def function1(parameters):
    print("This is function 1.")
    print(parameters)
          
