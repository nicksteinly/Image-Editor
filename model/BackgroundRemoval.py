import cv2
import numpy as np
from PIL import Image
from flask import Blueprint
from flask import jsonify, request

background_removal_bp = Blueprint('background_removal', __name__)

@background_removal_bp.route('/remove_black_background', methods=["POST"])
def remove_black_background_to_png():
    try:
      data = request.json
      input_image_path = data.get('inputImagePath')
      output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/black-background-removal.png'
      img = Image.open(input_image_path)
      rgba = img.convert("RGBA")
      datas = rgba.getdata()
        
      newData = []
      for item in datas:
          if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
              # storing a transparent value when we find a black colour
              newData.append((255, 255, 255, 0))
          else:
              newData.append(item)  # other colours remain unchanged
        
      rgba.putdata(newData)
      rgba.save(output_image_path, "PNG")
      return jsonify({'outputImage': rgba})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Remove Black Background Failed'})