# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import MeCab

app = Flask(__name__)

keys = {
    "hoge"
}

def is_valid_key(key):
    if key in keys:
        return True
    return False

@app.route("/")
def hello():
    return "Usage: ..."

@app.route('/api/1.0/analyze', methods=['POST'])
def analyze_post():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            key = request.json['key']
            if is_valid_key(key):
                text = request.json['text']
                m = MeCab.Tagger("-Owakati")
                return jsonify({ "status": "OK", "text": text, "result": m.parse(text)})
            else:
                return jsonify({ "status": "NG"})
        else:
            return jsonify({ "status": "NG"})
    else:
        return jsonify({ "status": "NG"})

@app.route('/api/0.1/analyze')
def analyze_get():
    key  = request.args.get('key')
    if is_valid_key(key):
        text = request.args.get('text')
        m = MeCab.Tagger("-Owakati")
        return jsonify({ "status": "OK", "text": text, "result": m.parse(text).replace(" \n", "")})
    else:
        return jsonify({ "status": "NG"})


if __name__ == '__main__':
    app.run()



@app.route('/api/1.0/extraction', methods=['POST'])
def extraction_post():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            key = request.json['key']
            if is_valid_key(key):
                text = request.json['text']
                m = MeCab.Tagger("-Owakati")
                m2 = MeCab.Tagger('')
                m2.parseToNode('')
                node = m2.parseToNode(text)
                features = []
                surfaces = []
                while node:
                    pos = node.feature.split(",")[0]
                    feature = node.feature.split(",")[6]
                    surface = node.surface
                    if pos == "名詞":
                        features.append(feature)
                        surfaces.append(surface)
                    elif pos == "動詞":
                        surfaces.append(surface)
                        features.append(feature)
                    node = node.next
                return jsonify({ "status": "OK", "text": text, "result": m.parse(text).replace(",", " ").replace(" \n", ""), "feature": ",".join(features).replace(",", " "), "surface": ",".joi$
            else:
                return jsonify({ "status": "NG"})
        else:
            return jsonify({ "status": "NG"})
    else:
        return jsonify({ "status": "NG"})
