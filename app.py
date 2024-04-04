from flask import Flask, request, send_file
from flask_cors import CORS
import io
from PIL import Image

app = Flask(__name__)

CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def hello():
    return "hello you are in root page"

@app.route('/message')
def message():
    return "hi message"


# Lazy loading for the object detection model
def get_model():
  from ultralytics import RTDETR
  model = RTDETR('best.pt')
  return model

@app.route('/upload', methods=['GET', 'POST'])
def table_image():
    if request.method == 'POST':
        img_file = request.files['the_file']

        # Use lazy-loaded model
        model = get_model()()

        img = Image.open(img_file)
        results = model(img)
        boxes = results[0].boxes
        lis = []
        for i in boxes.xyxy[0]:
            lis.append(i.item())

        x = int(lis[0])
        y = int(lis[1])
        x_end = int(lis[2])
        y_end = int(lis[3])

        im1 = img.crop((x, y, x_end, y_end))

        img_io = io.BytesIO()
        im1.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')

    return 'noo'

if __name__ == '__main__':
    app.run(debug=True)
