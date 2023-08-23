
from flask import render_template, session, request, url_for, flash, redirect
from website import app, db, bcrypt
from .forms import RegistrationForm, login
from .models import SPI, users
import os



@app.route('/') #pagina inicial

def home():
    return render_template ('admin/index.html', title= 'special issue')

@app.route('/login', methods=['GET', 'POST']) #ATUALIZADO
def loginform():
    form = login(request.form)
    if request.method == "POST" and form.validate():
        user = users.query.filter_by(usuario=form.usuario.data).first()
        
        if user and user.senha == form.senha.data:
            session['usuario'] = form.usuario.data
            flash(f'{form.usuario.data} entrou', 'message')
            return redirect(url_for('inserirnova'))
        else:
            flash('Usuário não encontrado ou senha incorreta', 'message')
            
    return render_template('admin/login.html', form=form, title='login')
    

@app.route('/inserirnovaspecialissue', methods=['GET', 'POST']) #pagina de adicionar novas s.i
def inserirnova():
    form = RegistrationForm(request.form)
    if request.method ==  'POST' and form.validate():
        specialissue= SPI(editora=form.editora.data, revista=form.revista.data, titulo=form.titulo.data, link=form.link.data,prazo=form.prazo.data,datanot=form.datanot.data, detalhes=form.detalhes.data)
        db.session.add(specialissue)
        db.session.commit()
        flash(f'Special Issue enviada!', 'message')
        return redirect(url_for('home'))
    return render_template('admin/inserirnova.html', form=form, title = "Página de envios")


        return redirect(url_for('home'))
    return render_template('admin/inserirnova.html', form=form, title = "Página de envios")
