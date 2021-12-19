import urllib.request
import sys
sys.path.insert(0, './lib')
import json
import Flask, request
app = Flask(__name__)

detector = ObjectDetector()

@app.route("/detect")
def detect_handle():
    image_url = request.args.get('image_url', None)
    result = detector.detect_img(image_url)
    json_string = json.dumps({"result": result})
    return json_string.encode(encoding='utf_8')

app.run(host="0.0.0.0", port=5000, threaded=True)
