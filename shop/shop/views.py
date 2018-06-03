from flask import request, render_template, redirect, abort, url_for
from pony.orm import ObjectNotFound

from . import app
from .forms import CustomerForm
from .models import Customer


@app.route('/registration')
def registration():
    form = CustomerForm(request.form)  # для редактироования еще используем объект из pony   --- obj=

    if form.validate_on_submit():  # проверяем, что форма отправлена методом POST и они валидные
        customer = Customer(email= form.email.data,
                            phone=form.phone.data,
                            name=form.name.data)

        return redirect(url_for('registration'))   # перенапрвляем на другую страницу, чтобы избежать постоянной перезагруки страницы пользователем

    return render_template('registration.html', form=form)  # отрисовать шаблон

