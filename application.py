from flask import Flask, render_template, request, jsonify, Response
import json
from flask_cors import CORS, cross_origin

application = Flask(__name__)

CORS(application)
cross_origin(application)

@application.route('/', methods=['GET', 'POST'])
def genome():
	return render_template('morpheus_tcga.html')

if __name__ == '__main__':
   application.run(host='0.0.0.0', debug = True)


