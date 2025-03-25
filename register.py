from flask import Flask, render_template, request, redirect, url_for
from data import db_session
from data.users import User
from werkzeug.security import generate_password_hash

app = Flask(__name__, template_folder='html')
app.config['SECRET_KEY'] = 'Enter_zlo'  # Добавляем SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Получаем данные из формы
        login = request.form['login']
        password = request.form['password']
        reset_password = request.form['reset_password']
        surname = request.form['surname']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        speciality = request.form['speciality']
        address = request.form['address']

        # Инициализируем сессию базы данных
        db_session.global_init("db/mars_explorer.db")  # Укажите путь к вашей базе данных
        db_sess = db_session.create_session()

        # Создаем нового пользователя
        user = User()
        user.surname = surname
        user.name = name
        user.age = age
        user.position = position
        user.speciality = speciality
        user.address = address
        user.email = login  # Используем login как email
        user.hashed_password = generate_password_hash(password)  # Хешируем пароль

        # Добавляем пользователя в сессию и сохраняем
        db_sess.add(user)
        db_sess.commit()

        return redirect(url_for('success'))  # Перенаправление на страницу успеха

    return render_template('register.html')

@app.route('/success')
def success():
    return "Регистрация прошла успешно!"

if __name__ == '__main__':
    app.run(debug=True)
