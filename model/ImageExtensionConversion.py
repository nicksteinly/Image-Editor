import cv2
import numpy as np
from PIL import Image
from flask import Blueprint
from flask import jsonify, request

extension_conversion_bp = Blueprint('extension_conversion', __name__)

@extension_conversion_bp.route('/jpg_to_png', methods=["POST"])
def jpg_to_png():
    try:
      data = request.json
      input_image_path = data.get('inputImagePath')
      output_image_path = data.get('outputImagePath')
        # Open the JPG image
      with Image.open(input_image_path) as img:
          # Convert and save the image as PNG
          img.save(output_image_path, format='PNG')
          return jsonify({'success': 'Image converted successfully from JPG to PNG.'})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'JPG to PNG failed'})