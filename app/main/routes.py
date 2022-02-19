from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from langdetect import detect, LangDetectException
from app import db
from app.main.forms import EditProfileForm, EmptyForm, CurrentStockForm, SearchForm, \
    MessageForm
from app.models import User, CurrentStock
from app.main import bp
from datetime import datetime, timezone

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    
    return render_template('index.html', title='Home')

@bp.route('/currentstocks', methods=['GET', 'POST'])
@login_required
def currentstocks():
    form = CurrentStockForm()
    if form.validate_on_submit():   
        try:
            stock = CurrentStock()
            form.populate_obj(stock)
            stock.user_id = current_user.id
            db.session.add(stock)
            db.session.commit()
            flash('Stock '+ form.ticker.data + ' was listed succesfully')
        except:
            flash('An error occurred. Stock ' + form.ticker.data + ' could not be listed.')
            db.session.rollback()      
    currentStocks = CurrentStock.query.filter_by(user_id=current_user.id)
    return render_template('currentstocks.html', currentStocks=currentStocks, form=form, title="Current Stocks")


@bp.route('/currentstocks/<current_stock_id>', methods=['POST'])
@login_required
def delete_current_stock(current_stock_id):
    form = CurrentStockForm()
    if (request.form['method'] == "DELETE"):
        stock = CurrentStock.query.get(current_stock_id)
        ticker = stock.ticker
        try:
            db.session.delete(stock)
            db.session.commit()
            flash('Stock ' + ticker + ' was successfully deleted!')
        except:
            db.session.rollback()
            flash('Stock ' + ticker + ' was successfully deleted!')

        currentStocks = CurrentStock.query.filter_by(user_id=current_user.id)
        return render_template('currentstocks.html', currentStocks=currentStocks, form=form, title="Current Stocks")

@bp.route('/currentstocks/<int:current_stock_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_current_stock(current_stock_id):
    stock = CurrentStock.query.get(current_stock_id)
    form = CurrentStockForm(obj=stock)
    if form.validate_on_submit():   
        try:
            form.populate_obj(stock)
            stock.user_id = current_user.id
            db.session.commit()
            flash('Stock '+ form.ticker.data + ' was updated succesfully')
        except:
            flash('An error occurred. Stock ' + form.ticker.data + ' could not be updated.')
            db.session.rollback()      
    currentStocks = CurrentStock.query.filter_by(user_id=current_user.id)
    return render_template('currentstocks.html', currentStocks=currentStocks, form=form, title="Current Stocks")

@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)

@bp.route('/user/<username>/popup')
@login_required
def user_popup(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/search')
@login_required
def search():
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)

@bp.route('/messages')
@login_required
def messages():
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/export_posts')
@login_required
def export_posts():
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/notifications')
@login_required
def notifications():
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)