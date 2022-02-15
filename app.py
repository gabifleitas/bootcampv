from flask import Flask, request, render_template, url_for 

app = Flask(__name__)

app.config['SECRET_KEY'] = '51dc30af-b37c-4b8a-90ea-4f32d6be3c78714'

@app.route('/', methods = ['GET', 'POST']) #crear la ruta para landing page
def home():
    return render_template('index.html')

@app.route('/bcampvirtual') #crear la ruta para el bootcamp virtual
def bootcamp():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '8888', debug = True)