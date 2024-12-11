from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from gtts import gTTS
from googletrans import Translator
import os

app = Flask(__name__)

CORS(app)
translator = Translator()


@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    try:

        data = request.get_json()
        text = str(data['text'])

        if not text or text == '':
            return jsonify({"Error": "Invalid input, 'text' are required"}), 400



        translate_text = translator.translate(text=text, dest='gu')

        tts = gTTS(translate_text.text, lang='gu')
        audio_file = "output.mp3"
        tts.save(audio_file)

        return send_file(audio_file, mimetype='audio/mp3')

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)
