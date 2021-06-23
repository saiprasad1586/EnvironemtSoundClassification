from flask import Flask, jsonify, url_for, request, render_template
import random
from get_result import Result
import os

UPLOAD_FOLDER = 'Uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
results = ['dog','chainsaw','crackling_fire','helicopter','rain', 'crying','clock_tick', 'sneezing','rooster','sea_waves']

@app.route('/', methods=['GET', "POST"])
def index():
    # filename = request.files['file'].filename
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    print(request.method)
    if request.method == 'POST':
        audio_file = request.files["file"]
        file_name = str(random.randint(0, 100000))
        file = file_name + '.wav'
        audio_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file))
        print(audio_file)
        file = file_name + '.wav'
        file = os.path.join(app.config['UPLOAD_FOLDER'] ,file)
        res = Result(file)
        result = res.getResult()
        print(file)
        return render_template('result.html', result1=result, result2 = results[result[0]], filename = file)
    return jsonify({"result": 1})


if __name__ == '__main__':
    app.run()
