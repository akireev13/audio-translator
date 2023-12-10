from flask import Flask, render_template, request, send_file
from google.cloud import translate_v2, texttospeech
import os
import time

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

