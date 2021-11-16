import os
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH = 'best_vgg16_model.h5'

model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    x = image.img_to_array(img)
    x = x/255
    x = np.expand_dims(x, axis=0)

    pred = model.predict(x)
    pred = np.argmax(pred, axis=1)
    arg_pred = pred[0]

    return 'Car brand is ' + os.listdir('Datasets/Test/')[arg_pred].capitalize()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        if not os.path.exists('uploads'):
            os.mkdir('uploads')
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(
            basepath, 'uploads', secure_filename(f.filename)
        )
        f.save(filepath)

        pred = model_predict(filepath, model)
        return pred
    return None

if __name__ == '__main__':
    app.run(debug=True)

