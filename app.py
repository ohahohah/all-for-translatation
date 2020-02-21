import urllib
import json

from flask import Flask, render_template, jsonify, request
from googletrans import Translator

app = Flask(__name__)

with open('config.json', 'r') as f:
    config = json.load(f)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    src_txt = request.form['src_txt']
    dest_google = translate_google(src_txt)
    dest_papago = translate_papago(src_txt)

    return jsonify({'google': dest_google, 'papago': dest_papago})


def translate_google(src_txt):
    translator = Translator()
    result = translator.translate(src_txt, dest='ko')

    return result.text


def translate_papago(src_txt):
    client_id = config['PAPAGO']['CLIENT_ID']
    client_secret = config['PAPAGO']['CLIENT_SECRET']

    txt = urllib.parse.quote(src_txt)
    src_lang = detect_lang_papago(txt)

    data = "source=" + src_lang + "&target=ko&text=" + txt + "&honorific=true"
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request_server = urllib.request.Request(url)
    request_server.add_header("X-Naver-Client-Id", client_id)
    request_server.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request_server, data=data.encode("utf-8"))

    rescode = response.getcode()
    if rescode == 200:
        json_res = json.loads(response.read().decode('utf-8'))
        result = json_res['message']['result']['translatedText']

    else:
        pass
        # print("Error Code:" + rescode)

    return result


def detect_lang_papago(txt):
    client_id = config['PAPAGO']['CLIENT_ID']
    client_secret = config['PAPAGO']['CLIENT_SECRET']

    data = "query=" + txt
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    request_server = urllib.request.Request(url)
    request_server.add_header("X-Naver-Client-Id", client_id)
    request_server.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request_server, data=data.encode("utf-8"))

    rescode = response.getcode()
    if rescode == 200:
        json_res = json.loads(response.read().decode('utf-8'))
        detected_lang = json_res['langCode']
    else:
        pass
        # print("Error Code:" + rescode)

    return detected_lang


if __name__ == '__main__':
    app.run()
