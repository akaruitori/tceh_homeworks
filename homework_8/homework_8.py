from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='Got a secret',
    WTF_CSRF_ENABLED=False,
)


# 1. По адресу /locales должен возвращаться массив в формате json с тремя
# локалями: ['ru', 'en', 'it']

@app.route('/locales')
def locales():
    return jsonify(['ru-RU', 'en-US', 'it-IT'])


# 2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе
# два числа, возвращать их сумму

@app.route('/sum/<int:first>/<int:second>')
def show_sum(first, second):
    return 'Sum is ' + str(first+second)


# 3. По адресу /greet/<user_name> должен получать имя пользователя,
# возвращать текст 'Hello, имя_которое_прислали'

@app.route('/greet/<user_name>')
def greet_user(user_name):
    return 'Hello, {}!'.format(user_name)


# 4. По адресу /form/user должен принимать POST запрос с параментрами:
# email, пароль и подтверждение пароля. Необходимо валидировать email,
# что обязательно присутствует, валидировать пароли, что они минимум
# 6 символов в длину и совпадают. Возрващать пользователю json вида:
# "status" - 0 или 1 (если ошибка валидации), "errors" - список ошибок,
# если они есть, или пустой список.

class SignUpForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Email()
    ])
    password = PasswordField(label='Password', validators=[
        validators.InputRequired()
    ])
    password2 = PasswordField(label='Confirm Password', validators=[
        validators.InputRequired()
    ])

    def validate_password(form, field):
        if not form.password.data == form.password2.data:
            raise ValidationError('Passwords must match.')
        elif len(form.password.data) < 6:
            raise ValidationError('Password must be at least 6 characters '
                                  'long.')


@app.route('/form/user', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        form = SignUpForm(request.form)
        return jsonify({
            'status': int(not form.validate()),
            'errors': form.errors
        })


# 5. По адресу /serve/<path:filename> должен возвращать содержимое
# запрашиваемого файла из папки ./files. Файлы можно туда положить любые
# текстовые. А если такого нет - 404

@app.route('/serve/<path:filename>')
def show_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return 'File not found.', 404


if __name__ == '__main__':
    app.run()
