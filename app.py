from flask import Flask, render_template, request, jsonify, Response
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
cross_origin(app)

@app.route('/', methods=['GET', 'POST'])
def genome():
	return render_template('morpheus_tcga.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)


