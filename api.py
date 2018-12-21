import primeradiant as pr

import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    text = request.form.get('text')
    result = pr.scan(text)
    return json.dumps(result)

if __name__ == '__main__':
    app.run()
