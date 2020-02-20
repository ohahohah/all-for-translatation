from flask import Flask, render_template, jsonify, request
from googletrans import Translator

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


def translate_google(src_txt):
    translator = Translator()
    result = translator.translate(src_txt, dest='ko')

    return result.text


@app.route('/translate', methods=['POST'])
def translate():
    src_txt = request.form['src_txt']
    dest_google = translate_google(src_txt)

    return jsonify({'google_txt': dest_google})


if __name__ == '__main__':
    app.run()
