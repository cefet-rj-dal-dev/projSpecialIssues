
#atualizado 07/12
from flask import render_template, session, request, url_for, flash, redirect, Flask
from website import app, db, bcrypt
from .forms import RegistrationForm, login
from .models import SPI, users
import os

app.secret_key='123456789'

@app.route('/home') #pagina inicial

def home():
    if 'usuario' not in session:
        flash (f'Login necessário', 'danger')
        return redirect(url_for('loginform'))
    else:
        per_page=10
        page=request.args.get('page',type=int, default=1)
        specialissues= SPI.query.order_by(SPI.prazo.asc()).paginate(page=page, per_page=per_page)       
        
    return render_template ('admin/home.html', title= 'gerenciar', specialissues= specialissues)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search-box']
        session['search_value'] = search_value  # Armazena na sessão
        search = f"%{search_value}%"
        specialissues = SPI.query.filter(SPI.titulo.like(search)).paginate(page=1, per_page=10)
        return render_template('admin/busca.html', specialissues=specialissues, search_value=search_value)
    else:
        page = request.args.get('page', 1, type=int)
        per_page = 10

        search_value = session.get('search_value', '')  # Obtém da sessão
        if page == 1 and search_value:
            specialissues = SPI.query.filter(SPI.titulo.like(f"%{search_value}%")).paginate(page=1, per_page=10)
        else:
            specialissues = SPI.query.paginate(page=page, per_page=per_page)

    return render_template('admin/busca.html', specialissues=specialissues, search_value=search_value)


@app.route('/', methods=['GET', 'POST']) 
def loginform():
    form = login(request.form)
    if request.method == "POST" and form.validate():
        user = users.query.filter_by(usuario=form.usuario.data).first()
        
        if user and user.senha == form.senha.data:
            session['usuario'] = form.usuario.data
            return redirect(url_for('home'))
        else:
            flash('Usuário não encontrado ou senha incorreta', 'danger')
            
    return render_template('admin/login.html', form=form, title='login')

    
    

@app.route('/inserirnovaspecialissue', methods=['GET', 'POST']) #pagina de adicionar novas s.i
def inserirnova():
    if 'usuario' not in session:
        flash (f'Login necessário', 'danger')
        return redirect(url_for('loginform'))
    else:
        form = RegistrationForm(request.form)
        if request.method ==  'POST' and form.validate():
            specialissue= SPI(editora=form.editora.data, revista=form.revista.data, titulo=form.titulo.data, link=form.link.data,prazo=form.prazo.data,datanot=form.datanot.data, detalhes=form.detalhes.data)
            db.session.add(specialissue)
            db.session.commit()
            sucesso=True
            if sucesso:
                if 'submit_and_back' in request.form:
                    return redirect('/home')
                elif 'submit_and_insert' in request.form:
                    return render_template('admin/inserirnova.html', form=form)
                else:
                    flash(f'todos os campos são obrigatórios!', 'danger')
            
        return render_template('admin/inserirnova.html', form=form, title = "Página de envios")
    
@app.route('/gerenciar', methods=['GET', 'POST'])
def gerenciar():
    if 'usuario' not in session:
        flash (f'Login necessário', 'danger')
        return redirect(url_for('loginform'))
    else:
        specialissues= SPI.query.all()       
        
    return render_template ('admin/gerenciar.html', title= 'gerenciar', specialissues= specialissues)

@app.route('/detalhes/<int:id>', methods=['GET'])
def detalhes(id):
    if 'usuario' not in session:
        flash('Login necessário', 'danger')
        return redirect(url_for('loginform'))
    else:
        spi = SPI.query.get(id)
        if spi:
            return render_template('admin/detalhes.html', spi=spi, title='Detalhes do Special Issue')
        else:
            flash('Special Issue não encontrado', 'danger')
            return redirect('/gerenciar')

@app.route('/editar/<int:id>', methods=['GET', 'POST']) 
def editar(id):
    if 'usuario' not in session:
        flash (f'Login necessário', 'danger')
        return redirect(url_for('loginform'))
    
    else:
        spi= SPI.query.get(id)
        form = RegistrationForm(request.form, obj=spi)
       
        
        if request.method == 'POST' and form.validate():
            editora = request.form.get('editora')
            revista = request.form.get('revista')
            titulo = request.form.get('titulo')
            link = request.form.get('link')
            prazo = request.form.get('prazo')
            datanot = request.form.get('datanot')
            spi.editora=editora
            spi.revista=revista
            spi.titulo=titulo
            spi.link=link
            spi.prazo= prazo
            spi.datanot=datanot
            form.populate_obj(spi)
            db.session.commit()
            if 'update' in request.form:
                
                flash('Special issue atualizada!', 'success')
                return redirect('/gerenciar')
                    
            elif 'cancel' in request.form:
                return redirect('/gerenciar')
            else:
                flash('Todos os campos são obrigatórios!', 'danger')

    return render_template('admin/editar.html', spi=spi, title="Editar", form=form)


@app.route('/deletar/<int:id>', methods=['GET', 'POST'])
def deletar(id):
    spi = SPI.query.get(id) 

    if request.method == 'GET':
        return render_template('admin/gerenciar.html', spi=spi)

    if request.method == 'POST':
        db.session.delete(spi)
        db.session.commit()
        flash('Special Issue excluída!', 'success') 
        return redirect('/gerenciar')
    return render_template('admin/gerenciar.html', spi=spi)
