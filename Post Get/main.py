from flask import Flask, render_template
from auth import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'world world world hello'


@app.route('/', methods=['GET', 'POST'])
def main():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        print(name, surname, email)
        return render_template('base.html', title='Главная страница',
                               form=form, message='You are authorized')
    return render_template('base.html', title='Главная страница',
                           form=form)


if __name__ == '__main__':
    app.run()
