import cv2
import numpy as np
from PIL import Image
from flask import Blueprint
from flask import jsonify, request
import base64

background_removal_bp = Blueprint('background_removal', __name__)

@background_removal_bp.route('/remove_black_background', methods=["POST"])
def remove_black_background_to_png(image_input):
    try:
        # Convert the NumPy array to a PIL Image object
        img = Image.fromarray(image_input)

        rgba = img.convert("RGBA")
        datas = rgba.getdata()

        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
                # storing a transparent value when we find a black colour
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)  # other colours remain unchanged

        # Create a new image with the modified data
        updated_img = Image.new("RGBA", img.size)
        updated_img.putdata(newData)

        # Save the updated image directly to the output path using the original 'img' variable
        output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/black-background-removal.png'
        updated_img.save(output_image_path, "PNG")

        # Convert the updated image back to a NumPy array
        updated_img_array = np.array(updated_img)

        # Encode the updated image as a base64 string
        _, encoded_image = cv2.imencode('.png', updated_img_array)
        base64_string = base64.b64encode(encoded_image).decode('utf-8')

        return updated_img_array, base64_string

    except Exception as e:
        print(e)
        return {'error': 'Remove Black Background Failed'}
