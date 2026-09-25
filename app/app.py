from flask import Flask, request, redirect, render_template_string
import psycopg2
import os

app = Flask(__name__)

# Подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host="db",           # имя сервиса в docker-compose
        database="myapp",
        user="admin",
        password="secret"
    )
    return conn

# Главная страница
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        cur.execute('INSERT INTO users (name) VALUES (%s)', (name,))
        conn.commit()
        return redirect('/')

    cur.execute('SELECT id, name FROM users ORDER BY id')
    users = cur.fetchall()
    cur.close()
    conn.close()

    html = '''
    <!DOCTYPE html>
    <html>
    <head><title>Мои пользователи</title></head>
    <body>
        <h1>Список пользователей</h1>
        <ul>
            {% for user in users %}
	    <li>{{ user[1] }} <a href="/delete/{{ user[0] }}">[x]</a></li>
            <li>{{ user[1] }}</li>
            {% endfor %}
        </ul>
        <form method="post">
            <input type="text" name="name" placeholder="Введите имя">
            <button type="submit">Добавить</button>
        </form>
    </body>
    </html>
    '''
    return render_template_string(html, users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

