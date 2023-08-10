import cv2
import numpy as np
import base64
from PIL import Image, ImageFilter, ImageEnhance
from flask import Blueprint
from flask import jsonify, request

recoloration_bp = Blueprint('recoloration', __name__)

def HEX_to_BGR(hex_color):
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return b, g, r

@recoloration_bp.route('/recolor_white_pixels', methods=["POST"])
def recolor_white_pixels(hex_color, image_input):
     # Convert hex color to RGB
    bgr_color = HEX_to_BGR(hex_color)
    print(type(image_input))
    print(len(image_input))
    print(np.shape(image_input))

    # Flatten the image array to 2D with 3 columns (RGB)
    flatted_image_array = image_input.reshape(-1, 3)
    print(np.shape(flatted_image_array))
    # Get the indices of white pixels
    white_pixels_indices = np.all(flatted_image_array == [255, 255, 255], axis=1)

    # Replace white pixels with the inputted color
    flatted_image_array[white_pixels_indices] = bgr_color

    # Reshape the flattened array back to the original image shape
    modified_image = flatted_image_array.reshape(image_input.shape)

    output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/recolored-white-pixels.png'
    cv2.imwrite(output_image_path, modified_image)
    _, encoded_image = cv2.imencode('.png', modified_image)
    base64_string = base64.b64encode(encoded_image).decode('utf-8')
    return image_input, base64_string


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
        target_color_bgr = HEX_to_BGR(target_color_hex)

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
        return filtered_image, base64_string

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
        target_color_bgr = HEX_to_BGR(target_color_hex)

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
        return filtered_image, base64_string

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'Filtering by color failed'})
    

def gaussian_blur(radius, image_input):
    # Apply Gaussian blur to the image
    # The higher the radius, the more blurred the image will be
    # The radius must be an odd integer because the center of the kernel is calculated at a single point, and an odd number ensures that there is a well-defined center.
    # The third argument is the standard deviation (of kernel) in the X direction. If it is 0, it is calculated automatically based on the kernel size.
    radius = int(radius)
    blurred_image = cv2.GaussianBlur(image_input, (radius, radius), 0)

    output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/gaussian-blur.png'
    cv2.imwrite(output_image_path, blurred_image)
    _, encoded_image = cv2.imencode('.png', blurred_image)
    base64_string = base64.b64encode(encoded_image).decode('utf-8')

    return blurred_image, base64_string

def sharpen(amount, radius, image_input):
    # Apply Gaussian blur (opposite of unblur) to simulate the original blurred image
    print("amount: ", amount)
    radius = int(radius)
    amount = float(amount)
    blurred_image = cv2.GaussianBlur(image_input, (radius, radius), 0)
    
    # Apply sharpening filter to enhance details and edges
    sharpened_image = cv2.addWeighted(image_input, 1 + amount, blurred_image, -amount, 0)
        

    output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/sharpen.png'
    cv2.imwrite(output_image_path, sharpened_image)
    _, encoded_image = cv2.imencode('.png', sharpened_image)
    base64_string = base64.b64encode(encoded_image).decode('utf-8')

    return sharpened_image, base64_string