from flask import Flask, redirect, url_for
from app_blueprint import blueprint
app = Flask(__name__)
app.register_blueprint(blueprint)

@app.route('/admin')
def admin():
    return redirect(url_for('h'))
if __name__ == '__main__':
    app.run()