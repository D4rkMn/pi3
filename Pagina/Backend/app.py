import os
import sys
sys.path.append('../../')
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from BrailleWrapper import procesarArchivo
UPLOAD_FOLDER = '../../Python/Input'
TEMPLATE_LOCATION = '../Frontend/templates'

app = Flask(__name__, template_folder=TEMPLATE_LOCATION)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/script.js')
def script():
    return render_template('script.js')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        procesarArchivo(filepath)
        return render_template('websocket.html')
    return 'File type not allowed', 400

if __name__ == "__main__":
    app.run(debug=True,port=5001)
