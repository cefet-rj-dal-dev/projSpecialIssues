from flask import render_template, session, request, url_for
from website import app, db

@app.route('/')

def home():
    return "special issues"

@app.route('/inserirnova')

def inserir():
    return render_template('admin/inserirnova.html', title="Inserir nova Special Issue")
