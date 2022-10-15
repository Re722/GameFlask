from crypt import methods
from flask import Flask, render_template,request,url_for
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    variavel = "Game : Adivinhe o numero correto para vencer o jogo!!"
    if request.method == "GET":
        return render_template("index.html",variavel=variavel)
    else:
        number = 0
        palpit = int(request.form.get("name"))
        if number == palpit:
            return '<h1>Voce ganhou</h1>'
        else:
            return '<h1>Voce perdeu</h1>'
     


@app.route('/<string:name>')
def error(name):
    variavel = f'Pagina {name} não existe'
    return render_template("error.html",variavel=variavel)