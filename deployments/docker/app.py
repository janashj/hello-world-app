
from flask import Flask,  jsonify 
import os 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return jsonify({
        'message': 'hello, I am devops, nice to meet you, happy debugging after school',
        'environment': os.environ.get('ENVIRONMENT'),
        'owner': 'janashj',
        'namespace': os.environ.get('NAMESPACE')
    })
@app.route('/soon')
def comming_soon():
    return jsonify({
        'message': 'This is comming soon page!!'
    })

# @app.route('/janarajorobaeva')
# def comming_soon():
#     return jsonify({
#         'message': 'This is Janara Jorobaeva, welcome a board!!'
#     })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
