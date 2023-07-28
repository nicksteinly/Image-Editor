import cv2
import numpy as np
from PIL import Image
from flask import Blueprint
from flask import jsonify, request

recoloration_bp = Blueprint('recoloration', __name__)

@recoloration_bp.route('/recolor_white_pixels', methods=["POST"])
def recolor_white_pixels():
    try:
      data = request.json
      image_path = data.get('inputImagePath')
      hex_color = data.get('hexColor')
      # Read the image
      image = cv2.imread(image_path)

      # Convert the hex color to BGR format (OpenCV uses BGR instead of RGB)
      color_bgr = tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))

      # Find white pixels (assume that white is close to [255, 255, 255] in BGR)
      white_mask = np.all(image == [255, 255, 255], axis=-1)

      # Replace white pixels with the specified color
      image[white_mask] = color_bgr
      output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/recolored-white-pixels.png'
      cv2.imwrite(output_image_path, image)
      return jsonify({'outputImagePath': output_image_path})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'White Pixels to Color Failed'})
      