
from flask import Flask,  jsonify 
import os 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return jsonify({
        'message': 'hello, I am devops, nice to meet you, ENjoy your night debuggings ;) !',
        'environment': os.environ.get('ENVIRONMENT'),
        'owner': 'janashj',
        'namespace': os.environ.get('NAMESPACE')
    })

@app.route('/jorobaeva')
def jorobaeva():
    return jsonify({
        'message': 'This is Janara Jorobaeva, welcome a board!!'
    })

@app.route('/soon')
def comming_soon():
    return jsonify({
        'message': 'This is comming soon page!!'
    })

@app.route('/qa')
def qa_page():
    return jsonify({
        'message': 'This is QAs page!!'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
