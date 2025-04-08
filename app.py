from flask import Flask 

app = Flask(__name__)

@app.routel("/", methods=['GET'])
def home():
    return "<h1>Jesvi's Flas App</h1>"

if __name__ == "__main__":
    app.run()