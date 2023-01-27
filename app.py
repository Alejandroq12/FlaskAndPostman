#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

greetings = {
            'en': 'hello', 
            'es': 'Hola', 
            'ar': 'مرحبا',
            'ru': 'Привет',
            'fi': 'Hei',
            'he': 'שלום',
            'ja': 'こんにちは'
            }

@app.route('/greeting', methods=['GET'])
def greeting_all():
    return jsonify({'greetings': greetings})

@app.route('/greeting/<lang>', methods=['GET'])
def greeting_one(lang):
    print(lang)
    if(lang not in greetings):
        abort(404)
    return jsonify({'greeting': greetings[lang
    ]})

@app.route('/greeting', methods=['POST'])
def greeting_add():
    info = request.get_json()
    if('lang' not in info or 'greeting' not in info):
        abort(422)
    greetings[info['lang']] = info['greeting']
    return jsonify({'greetings':greetings})

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)