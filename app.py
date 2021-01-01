from flask import Flask, render_template
from flask import request, url_for
from flask import request, current_app
from flask_restful import Resource, Api

app = Flask(__name__, static_folder='./static', template_folder='./templates')

@app.route('/', methods = ['POST', 'GET', 'OPTIONS'])
def tensorboard():
 	return render_template('tensorboard.html')

if __name__ == "__main__":
    app.run()
