from flask import Flask


app = Flask(__name__)
    

# api routes
@app.route('/api')
def api():
    return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)