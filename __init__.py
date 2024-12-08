from flask import Flask, redirect, url_for, render_template

from app_blueprint import blueprint
app = Flask(__name__)
app.register_blueprint(blueprint)

@app.route('/')
def whatever():
    return render_template('home.html', )

@app.route('/admin')
def admin():
    return redirect(url_for('h'))


if __name__ == '__main__':
    app.run(debug=True)