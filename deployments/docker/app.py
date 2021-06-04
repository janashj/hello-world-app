
from flask import Flask,  jsonify 
import os 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return jsonify({
        'message': 'hello world',
        'environment': os.environ.get('ENVIRONMENT'),
        'namespace': os.environ.get('NAMESPACE')
    })
@app.route('/soon')
def comming_soon():
    return jsonify({
        'message': 'This is comming soon page!!'
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

