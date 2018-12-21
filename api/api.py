import primeradiant as pr

import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url')
    text = pr.url_to_text(url)
    result = pr.scan(text)
    return json.dumps(result)

if __name__ == '__main__':
    app.run()
