from crypt import methods
from flask import Flask, render_template, request, url_for
from helper_function import generate_poem, generate_film
import sys 

app = Flask(__name__)

poem = ''
plot = ''

@app.route('/', methods=['POST', 'GET'])

def home():
    global poem
    global plot

    if request.method == 'POST':
        if 'poem input' in request.form:
        # poem input form and calling poem generator function
    
            user_input_poem = request.form["poem input"]
            poem = generate_poem(user_input_poem)
            return render_template('main.html', poem = poem, plot=plot)

        # film input form and calling poem generator function

        elif 'film input' in request.form:
            user_input_film = request.form["film input"]
            plot = generate_film(user_input_film)
            return render_template('main.html', plot = plot, poem=poem)
    
    else:
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, port = 3009)