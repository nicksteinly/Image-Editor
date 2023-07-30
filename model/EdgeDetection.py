import cv2
import numpy as np
from PIL import Image
from flask import Blueprint
from flask import jsonify, request
import base64

edge_detection_bp = Blueprint('edge_detection', __name__)

@edge_detection_bp.route("/edge_detection_Canny", methods=["POST"])
def edge_detection_Canny(image_input):
    try:
      # data=request.json
      # image_path = data.get('imagePath')
      # Read the image and convert it to grayscale
      image = cv2.cvtColor(image_input, cv2.IMREAD_GRAYSCALE)

      # Apply Canny edge detection
      edges = cv2.Canny(image, 100, 200)
      output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/canny.png'
      cv2.imwrite(output_image_path, edges)
      _, encoded_image = cv2.imencode('.png', edges)
      base64_string = base64.b64encode(encoded_image).decode('utf-8')
      return edges, base64_string
    
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'Canny Edge Detection Failed'})

@edge_detection_bp.route("/outer_outline_detection", methods=["POST"])
def outer_outline_detection(image_input):
    # Read the image and convert it to grayscale
    try:
      # data=request.json
      # image_path = data.get('imagePath')
      image = image_input
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # Apply GaussianBlur to reduce noise and improve edge detection
      blurred = cv2.GaussianBlur(gray, (5, 5), 0)

      # Use Canny edge detection to find edges in the image
      edges = cv2.Canny(blurred, 100, 200)

      # Find contours in the edge-detected image
      contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

      # Draw the outer contours on a blank canvas
      outer_contours_img = np.zeros_like(image)
      cv2.drawContours(outer_contours_img, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

      # Convert the image to grayscale
      outer_contours_gray = cv2.cvtColor(outer_contours_img, cv2.COLOR_BGR2GRAY)

      # Threshold the image to obtain binary outline
      _, outer_outline = cv2.threshold(outer_contours_gray, 1, 255, cv2.THRESH_BINARY)
      output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/outer-outline.png'
      cv2.imwrite(output_image_path, outer_outline)
      _, encoded_image = cv2.imencode('.png', outer_outline)
      base64_string = base64.b64encode(encoded_image).decode('utf-8')
      return outer_outline, base64_string
    
    except Exception as e:
      print("Error:", e)
      return jsonify({'error': 'Outer Outline Detection Failed'})

@edge_detection_bp.route('/thickened_edges', methods=['POST'])
def thickened_edges(iterations, kernel_size, image_input):
    try:
        # data = request.json
        # image_path = data.get('imagePath')
        # kernel_size = data.get('kernelSize')
        # iterations = data.get('iterations')
        iterations_int = int(iterations)
        kernel_size_int = int(kernel_size)
        # Read the image and convert it to grayscale
        image = image_input

        # Apply Canny edge detection
        edges = cv2.Canny(image, 100, 200)

        # Create a kernel for dilation
        kernel = np.ones((kernel_size_int, kernel_size_int), np.uint8)

        # Dilate the edges to thicken them
        thick_edges = cv2.dilate(edges, kernel, iterations=iterations_int)

        # Convert NumPy ndarray to list for JSON serialization
        output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/thickened.png'
        cv2.imwrite(output_image_path, thick_edges)
        _, encoded_image = cv2.imencode('.png', thick_edges)
        base64_string = base64.b64encode(encoded_image).decode('utf-8')
        return thick_edges, base64_string

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'Thicken Edges Failed'})

