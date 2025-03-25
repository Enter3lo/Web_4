from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Здесь вы можете обработать данные формы
        login = request.form['login']
        password = request.form['password']
        reset_password = request.form['reset_password']
        surname = request.form['surname']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        speciality = request.form['speciality']
        address = request.form['address']
        
        # Здесь можно добавить логику для сохранения данных пользователя в базу данных

        return redirect(url_for('success'))  # Перенаправление на страницу успеха

    return render_template('html/register.html')

@app.route('/success')
def success():
    return "Регистрация прошла успешно!"

if __name__ == '__main__':
    app.run(debug=True)
