from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__, static_folder='static')


def get_models():
    with open('static/glasses_models/glasses_models_names.json') as json_file:
        return json.loads(json_file.read())


@app.route('/', methods=['GET', 'POST'])
def index():
    models = get_models()
    if request.method == 'POST':
        return render_template('index.html', model=models[request.form.get('model')], models=models.keys())
    return render_template('index.html', models=models.keys())


app.run()
