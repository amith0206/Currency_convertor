from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/algorithm')
def algorithm():
    return render_template('algorithm.html')

@app.route('/product')
def index():
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True)
