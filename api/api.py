import primeradiant as pr

import json
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/scan', methods=['POST'])
def scan():
    print(request.get_json())
    url = request.get_json()['url']
    print(url)
    text = pr.url_to_text(url)
    result = pr.scan(text)
    return json.dumps(result)

if __name__ == '__main__':
    app.run()
