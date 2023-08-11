
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import skimage.feature as imf
import urllib.request
from os import path as osp
from matplotlib import pyplot as plt
import skimage.io as io
from flask import Flask, jsonify, request, Blueprint
import base64
import io as io_module
import cv2

coins_bp = Blueprint('/object-detection/template-matching/coins', __name__)

plt.switch_backend("Agg")

def retrieve(file_name, semester='spring23', homework=1):
    if osp.exists(file_name):
        print('Using previously downloaded file {}'.format(file_name))
    else:
        fmt = 'https://www2.cs.duke.edu/courses/{}/compsci527/homework/{}/{}'
        url = fmt.format(semester, homework, file_name)
        urllib.request.urlretrieve(url, file_name)
        print('Downloaded file {}'.format(file_name))

def show_ncx_maxima(ncx, max_points, title):
    plt.imshow(ncx)
    plt.plot(max_points[:, 1], max_points[:, 0], '.r')
    plt.axis('off')
    plt.title(title)
    buf = io_module.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def show_max_args(args, colors, title):
    ax = plt.gca()
    colormap = ListedColormap(colors)
    ax.pcolor(args, cmap=colormap)
    plt.axis('image')
    plt.axis('off')
    ax.invert_yaxis()
    plt.title(title)
    buf = io_module.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def show_overall_maxima(ncx_max, ncx_arg, max_points, info):
    title = 'maximum correlation over coin types'
    ncx_maxima_image = show_ncx_maxima(ncx_max, max_points, title)
    colors = [i['color'] for i in info.values()]
    max_args_image = show_max_args(ncx_arg, colors, title)
    return [ncx_maxima_image, max_args_image]

@coins_bp.route('/label_coins', methods=['GET'])
def label_coins():
    for name in ('coins', 'nickel', 'dime', 'quarter'):
        retrieve(name + '.png')

    coins = io.imread('coins.png')
    coin_info = {
        'nickel': {'color': 'yellow', 'value': 5},
        'dime': {'color': 'orange', 'value': 10},
        'quarter': {'color': 'red', 'value': 25},
    }
    plts = [encode_image_to_base64(coins)]

    maxima_threshold = 0.5
    min_distance = 80  # a little more than half of the template image size

    for index, coin_name in enumerate(coin_info.keys()):
        coinTemplate = io.imread(coin_name + '.png')
        ncc = imf.match_template(coins, coinTemplate, pad_input=True)
        maxima = imf.peak_local_max(ncc, min_distance=min_distance, threshold_abs=maxima_threshold)
        coin_info[coin_name]['ncc'] = ncc
        encoded_ncx = show_ncx_maxima(ncc, maxima, coin_name)
        plts.append(encoded_ncx)

    ncc_stack = np.stack(list(coin_info[name]['ncc'] for name in coin_info))
    ncc_max = np.max(ncc_stack, axis=0)
    ncc_arg = np.argmax(ncc_stack, axis=0)
    full_maxima = imf.peak_local_max(ncc_max, min_distance=min_distance, threshold_abs=maxima_threshold)
    max_images = show_overall_maxima(ncc_max, ncc_arg, full_maxima, coin_info)
    plts.append(max_images[0])
    plts.append(max_images[1])

    plt.imshow(coins, cmap=plt.cm.gray)
    money = 0
    for maxima in full_maxima:
        coin_type = list(coin_info)[ncc_arg[maxima[0]][maxima[1]]]
        plt.text(maxima[1], maxima[0], coin_type, color=coin_info[coin_type]['color'],
                ha='center', va='center', weight='bold')
        coin_info[coin_type]['count'] = coin_info[coin_type].get('count', 0) + 1
        money += coin_info[coin_type]['value']
    plt.title('Labeled Coins')
    plt.axis('off')
    plt.show()

    buf = io_module.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    labeled_coins_plot = base64.b64encode(buf.getvalue()).decode('utf-8')
    plts.append(labeled_coins_plot)

    money = 0
    for coin in coin_info.values():
        money += coin.get('value', 0) * coin.get('count', 0)
    total_value = money / 100
    coin_count = {coin: info['count'] for coin, info in coin_info.items()}
    return {"plots": plts, "total_value": f"${total_value:.2f}", "coin_count": coin_count}

def encode_image_to_base64(image):
    _, encoded_image = cv2.imencode('.png', image)
    base64_string = base64.b64encode(encoded_image).decode('utf-8')
    return base64_string

if __name__ == '__main__':
    result = label_coins()
    print(result)
