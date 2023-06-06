from flask import Flask, render_template
from groupes_de_requetes import groupe1,groupe2,groupe3,groupe4,groupe5
app = Flask(__name__)

@app.route('/')

def index ():
    return render_template(
        'index.html',
            group1 = groupe1.rendeur_de_requetes(),
            group2 = groupe2.rendeur_de_requetes(),
            group3 = groupe3.rendeur_de_requetes(),
            group4 = groupe4.rendeur_de_requetes(),
            group5 = groupe5.rendeur_de_requetes()
   )
