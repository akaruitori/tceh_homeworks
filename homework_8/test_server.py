from flask import Flask, request

from flask_wtf import FlaskForm
from wtforms import StringField, validators
from random import randint

"""
Задача:
- написать веб сервер, который по адресу /random будет отдавать
рандомное число
- написать route по адресу /submit будет принимать POST запрос,
в котором должны быть:
1. Паспортный номер: 10 цифр
2. Имя: Три слова
3. Дата рождения в формате: DD.MM.YYYY
"""


class ContactForm(FlaskForm):
    id_number = StringField(label='ID', validators=[
        validators.Length(min=10, max=10)
    ])
    name = StringField(label='Full Name', validators=[
        validators.Regexp(r'(\w+ \w+ \w+)')
    ])
    date_of_birth = StringField(label='Date of Birth', validators=[
        validators.Regexp(r'(\d{2}.\d{2}.(19|20)\d{2})')
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

@app.route('/random')
def random_number():
    return randint(0, 100)


@app.route('/submit', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())
        return ('valid', 200) if form.validate() else ('invalid', 400)
    return 'hello world!', 200

if __name__ == '__main__':
    app.run()
