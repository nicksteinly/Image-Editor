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
    
def overlay_image_with_mask(image_input, mask_image_path):

    # Load the mask image (the image you want to use as the filter)
    mask_image = cv2.imread(mask_image_path, 0)  # Use 0 to load the mask as grayscale

    # Resize the mask image to match the size of the input image (if needed)
    mask_image = cv2.resize(mask_image, (image_input.shape[1], image_input.shape[0]))

    # Create the inverted mask
    mask_inverted = cv2.bitwise_not(mask_image)

    # Convert the mask to 3 channels to match the input image
    mask_rgb = cv2.merge((mask_inverted, mask_inverted, mask_inverted))

    # Use bitwise_and to filter out the area specified by the mask
    filtered_image = cv2.bitwise_and(image_input, mask_rgb)
    output_image_path = '/Users/nicholassteinly/Library/CloudStorage/OneDrive-DukeUniversity/portfolio/Image-Editor/view/src/resources/images/overlayed-image-with-mask.png'
    cv2.imwrite(output_image_path, filtered_image)
    _, encoded_image = cv2.imencode('.png', filtered_image)
    base64_string = base64.b64encode(encoded_image).decode('utf-8')
    return filtered_image, base64_string