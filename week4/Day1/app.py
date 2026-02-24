from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'welcom to my basic backend flask project!'
if __name__ == '__main__':
    app.run(debug=True)
