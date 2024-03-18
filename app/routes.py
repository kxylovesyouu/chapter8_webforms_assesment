from app import app
from flask import render_template, flash, redirect, url_for
from flask import render_template
from app.forms import RegisterForm, AddProductForm


@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('shop.html', title='Shop Page')
    
@app.route('/add_product', methods=['GET','POST'])
def add_product():
    """Index URL"""
    form =AddProductForm()
    if form.validate_on_submit():
        flash(f'You have added {form.product_name.data}')
        return redirect(url_for('index'))
    return render_template('add_product.html', title='Add Product', form=form)
    

    
@app.route('/register', methods=['GET','POST'])
def register():
    """Index URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You have been succsesfully registered! {form.username.data}')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register Page', form=form)

# 