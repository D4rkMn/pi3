import os

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from BrailleWrapper import procesarArchivo

ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = 'Python/Input'
TEMPLATE_LOCATION = 'Pagina/Frontend/templates'

app = Flask(__name__, template_folder=TEMPLATE_LOCATION)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    print(os.getcwd())
    return render_template('index.html')

@app.route('/script.js')
def script():
    return render_template('script.js')

@app.route('/upload', methods=['POST'])
def upload_file():
    print("printea")
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        procesarArchivo(filepath)
        return render_template('websocket.html')
    return 'File type not allowed', 400

if __name__ == "__main__":
    app.run(debug=True,port=5001)
