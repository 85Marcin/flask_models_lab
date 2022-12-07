from flask import render_template
from app import app
from models.order_list import order_list

@app.route('/orders')
def index():
    return render_template('index.html', title='Orders', order_list=order_list)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', title='Order', order_list= order_list ,index=index)
