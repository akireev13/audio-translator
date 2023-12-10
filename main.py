from flask import Flask, render_template, request, send_file
from google.cloud import translate_v2, texttospeech
import os
import time

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html', translated_text=None, audio_file=None)




if __name__ == '__main__':
    app.run(debug=True)

