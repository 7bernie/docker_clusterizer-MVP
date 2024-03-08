#!/usr/bin/python3
""" Script that is main entry point of Flask application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


@app.route('/monitor')
def monitor():
    return render_template('monitor.html')


@app.route('/scale')
def scale():
    return render_template('scale.html')


@app.route('/docs')
def documentation():
    return render_template('documentation.html')


if __name__ == '__main__':
    app.run(debug=True)
