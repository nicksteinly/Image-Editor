import cv2
import numpy as np
import base64
from PIL import Image
from flask import Blueprint
from flask import jsonify, request

recoloration_bp = Blueprint('recoloration', __name__)

@recoloration_bp.route('/recolor_white_pixels', methods=["POST"])
def recolor_white_pixels(hex_color, image_input):
    """
    Recolor white pixels in the input image to a specified color.

    Input JSON:
    {
        "inputImagePath": "path/to/input/image.png",
        "hexColor": "#RRGGBB"
    }

    The function replaces all white pixels (RGB value [255, 255, 255]) in the input image with the color specified
    by 'hexColor'. The target color should be given in hex format (e.g., "#RRGGBB").

    Output JSON:
    {
        "outputImagePath": "path/to/output/image.png"
    }
    """
    try:
    #   data = request.json
    #   image_path = data.get('inputImagePath')
    #   hex_color = data.get('hexColor')
      # Read the image
      image = image_input

      # Convert the hex color to BGR format (OpenCV uses BGR instead of RGB)
      color_bgr = tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))

      # Find white pixels (assume that white is close to [255, 255, 255] in BGR)
      white_mask = np.all(image == [255, 255, 255], axis=-1)

      # Replace white pixels with the specified color
      image[white_mask] = color_bgr
      output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/recolored-white-pixels.png'
      cv2.imwrite(output_image_path, image)
      _, encoded_image = cv2.imencode('.png', image)
      base64_string = base64.b64encode(encoded_image).decode('utf-8')
      return base64_string
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'White Pixels to Color Failed'})

@recoloration_bp.route('/filter_out_color', methods=['POST'])
def filter_out_color(target_color_hex, threshold, image_input):
    """
    Filter out colors similar to the target color from the input image.

    Input JSON:
    {
        "inputImagePath": "path/to/input/image.png",
        "targetColor": "#RRGGBB",
        "threshold": 30
    }

    The function creates a mask by comparing each pixel's color in the input image with the specified 'targetColor'.
    If the Euclidean distance between a pixel's color and the 'targetColor' is less than or equal to 'threshold',
    the pixel is considered similar to the target color and is filtered out. A higher 'threshold' value results in
    a more lenient filtering, preserving more colors in the output image.

    Output JSON:
    {
        "outputImagePath": "path/to/output/image.png"
    }
    """
    try:
        # data = request.json
        # image_path = data.get('inputImagePath')
        # target_color_hex = data.get('targetColor')
        # threshold = data.get('threshold',30)

        threshold_int = float(threshold)

        # Convert the target color from hex to BGR format
        target_color_bgr = hex_to_bgr(target_color_hex)

        # Convert the image to the HSV color space
        image = image_input
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Convert the target color to HSV format
        target_color_hsv = cv2.cvtColor(np.uint8([[target_color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]

        # Define the lower and upper bounds of the target color in HSV
        lower_bound = np.array([target_color_hsv[0] - threshold_int, 100, 100])
        upper_bound = np.array([target_color_hsv[0] + threshold_int, 255, 255])

        # Create a mask using the inRange function to filter the target color
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

        # Use the mask to set the target color pixels to black (0,0,0)
        filtered_image = image.copy()
        filtered_image[mask != 0] = [0, 0, 0]

        output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/filtered-color-out.png'
        cv2.imwrite(output_image_path, filtered_image)
        _, encoded_image = cv2.imencode('.png', filtered_image)
        base64_string = base64.b64encode(encoded_image).decode('utf-8')
        return base64_string

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'Filtering out of color failed'})

@recoloration_bp.route('/filter_by_color', methods=['POST'])
def filter_by_color(target_color_hex, threshold, image_input):
    """
    Filter the input image to keep only colors similar to the target color.

    Input JSON:
    {
        "inputImagePath": "path/to/input/image.png",
        "targetColor": "#RRGGBB",
        "threshold": 30
    }

    The function creates a mask by comparing each pixel's color in the input image with the specified 'targetColor'.
    If the Euclidean distance between a pixel's color and the 'targetColor' is less than or equal to 'threshold',
    the pixel is kept in the output image; otherwise, it is filtered out. A higher 'threshold' value results in a
    more lenient filtering, retaining more colors in the output image that are within the target threshold.

    Output JSON:
    {
        "outputImagePath": "path/to/output/image.png"
    }
    """
    try:
        # data = request.json
        # input_image_path = data.get('inputImagePath')
        # target_color_hex = data.get('targetColor')
        # threshold = data.get('threshold', 30)

        threshold_int = float(threshold)

        # Convert the target color from hex to BGR format
        target_color_bgr = hex_to_bgr(target_color_hex)

        # Read the input image
        image = image_input

        # Calculate the Euclidean distance between each pixel and the target color
        color_distances = np.linalg.norm(image - target_color_bgr, axis=-1)

        # Create a mask based on the color distances within the target threshold
        mask = color_distances <= threshold_int

        # Invert the mask to include pixels outside the target threshold
        mask = ~mask

        # Filter out pixels outside the target threshold by setting them to black (0,0,0)
        filtered_image = image.copy()
        filtered_image[mask] = [0, 0, 0]

        output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/filtered-by-color.png'
        cv2.imwrite(output_image_path, filtered_image)
        _, encoded_image = cv2.imencode('.png', filtered_image)
        base64_string = base64.b64encode(encoded_image).decode('utf-8')
        return base64_string

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'Filtering by color failed'})
    

def hex_to_bgr(hex_color):
  # Convert hex color (e.g., "#RRGGBB") to BGR format (OpenCV uses BGR instead of RGB)
  r = int(hex_color[1:3], 16)
  g = int(hex_color[3:5], 16)
  b = int(hex_color[5:7], 16)
  return [b, g, r]  # OpenCV uses BGR format