from flask import Flask
from flask_cors import CORS, cross_origin
from generate_summary import summarizeText

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/summarize/<string:text>', methods=['GET'])
def summarize(text):
    result = summarizeText(text)
    print ('Summary:\n', result)
    return result

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)