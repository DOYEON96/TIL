from flask import Flask, render_template, url_for, request
#from flask_ngrok import run_with_ngrok   # https://ngrok.com/docs
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
#run_with_ngrok(app)

@app.route("/", methods=['GET'])
def index_main_loading():
    return render_template("index.html")

## 파일 업로드 및 화면 출력
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global file
    if request.method == 'POST':
        print(os.getcwd())
        file = request.files['file']
        fname=file.filename
        print(fname)
        print(os.getcwd())
        file.save('./multi/0804/static/'+fname)
        return render_template('index.html', fname=fname)

if __name__ == "__main__":
    app.run()
