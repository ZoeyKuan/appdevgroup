from flask import Flask, redirect, url_for, render_template
# from app_blueprint import blueprint # app.register_blueprint(blueprint)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calendar')
def cale():
    return render_template('calendar.html')

if __name__ == '__main__':
    app.run(debug=True)