from .config.config import config
from flask import Flask, request
import json

def create_app(config_name):
    from .lib.detector import ObjectDetector
    detector = ObjectDetector()
    app = Flask(__name__)
    # app.config.from_object(config[config_name])

    @app.route("/detect", methods=['GET'])
    def detect_handle():
        image_url = request.args.get('image_url', None)
        result = detector.detect_img(image_url)
        json_string = json.dumps({"result": result})
        return json_string.encode(encoding='utf_8')

    @app.cli.command()
    def test():
        import unittest
        import sys

        tests = unittest.TestLoader().discover("tests")
        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.errors or result.failures:
            sys.exit(1)

    return app
