from jinja2 import Template
from flask import render_template,request, send_file, url_for, Flask
app = Flask(__name__)

title_site = "піццерії Oderman!"
info = ["My fist site"]

@app.route("/")
def main_page():
    return render_template("base1.html", title=title_site, info=info)



@app.route('/')
def index():
    pizzas = [
        {'name': 'Маргарита', 'ingredients': 'шось складне', 'price': 180, 'weight': '300г'},
        {'name': 'Салямі', 'ingredients': 'Шось складне', 'price': 210, 'weight': '450г'}
    ]
    return render_template('test.html', pizzas=pizzas)



app.run()

