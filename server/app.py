from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# api routes
@app.route('/api')
def api():
    data = {'hello': 'world'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)