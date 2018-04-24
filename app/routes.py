from flask import request, render_template, session, redirect, url_for, flash
from app import app, db
from app.models.model_def import Accounts, Purchases


@app.route('/index')
def index():
    if session.get('logged_in'):
        username = session['username']
        current_purchase = Purchases.query.filter_by(username=username).first()
        return render_template('index.html', amount=current_purchase.count)
    else:
        return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    user = Accounts.query.filter_by(username=username, password=password).first()
    if user is None:
        flash('wrong username/password!')
        return redirect(url_for('login'))
    else:
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('index'))


@app.route('/purchase', methods=['POST'])
def purchase():
    username = session['username']
    current_purchase = Purchases.query.filter_by(username=username).first()
    if current_purchase is None:
        current_purchase = Purchases(username=username, count=1)
        db.session.add(current_purchase)
        db.session.commit()
    else:
        current_purchase.count += 1
        db.session.merge(current_purchase)
        db.session.commit()

    return render_template('thank_you.html', amount=current_purchase.count)


@app.route('/account/add', methods=['POST'])
def add_account():
    username = request.form['username']
    password = request.form['password']
    user = Accounts(username=username, password=password)
    db.session.add(user)
    db.session.commit

    return redirect(url_for('login'))
