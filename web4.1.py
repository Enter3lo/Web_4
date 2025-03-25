from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)


def main():
    # Инициализация базы данных
    db_session.global_init("C:/Users/sajhu/Desktop/Новая папка (2)/Web_4/db/mars_explorer.db")

    # Запуск приложения
    app.run(debug=True)


@app.route('/')
def works_log():
    # Получение списка работ из базы данных
    session = db_session.create_session()

    # Получаем все работы и информацию о руководителях
    jobs = session.query(Jobs).join(User, Jobs.team_leader == User.id).all()
    for i in range(len(jobs)):
        result = f'''<div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Activity
                        <div class="row">
                            <div class="col-md-6">
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">
                                        <strong>Team Leader:</strong> {jobs[i].team_leader}
                                    </li>
                                    <li class="list-group-item">
                                        <strong>Duration:</strong> {jobs[i].duration}
                                    </li>
                                    <li class="list-group-item">
                                        <strong>Collaborators:</strong> {jobs[i].collaboration}
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>'''

    return render_template('templates/works_log.html', actions='sywdyd')


if __name__ == '__main__':
    main()
