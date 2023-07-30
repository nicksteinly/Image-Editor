from flask import Flask
from flask_cors import CORS
from BackgroundRemoval import background_removal_bp
from EdgeDetection import edge_detection_bp
from ImageExtensionConversion import extension_conversion_bp
from Recoloration import recoloration_bp
from Operations import operations_bp

app = Flask(__name__)
app.debug = True
# Enable CORS for all domains on all routes which is not recommended for production because it is a security risk
CORS(app, origins="*")
app.register_blueprint(operations_bp, url_prefix='/operations')
app.register_blueprint(background_removal_bp, url_prefix='/background_removal')
app.register_blueprint(edge_detection_bp, url_prefix='/edge_detection')
app.register_blueprint(extension_conversion_bp, url_prefix='/extension_conversion')
app.register_blueprint(recoloration_bp, url_prefix='/recoloration')


if __name__ == "__main__":
    app.run(debug=True)