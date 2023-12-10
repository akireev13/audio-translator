from flask import Flask, render_template, request, send_file
from google.cloud import translate_v2, texttospeech
import os
import time

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './key.json'

translate_client = translate_v2.Client()
tts_client = texttospeech.TextToSpeechClient()

SUPPORTED_GENDER_LANGUAGES = {
    'pl': None,
    'en': texttospeech.SsmlVoiceGender.NEUTRAL,  
    'ru': texttospeech.SsmlVoiceGender.FEMALE, 
    'es': None,  
    'fr': None,  
}


@app.route('/')
def default():
    return render_template('index.html', translated_text=None, audio_file=None)




if __name__ == '__main__':
    app.run(debug=True)

