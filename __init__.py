from flask import Flask, redirect, url_for, render_template, request, flash
import shelve
import datetime
from app_blueprint import blueprint
app = Flask(__name__)
app.secret_key = 'secret_key'
app.register_blueprint(blueprint)


@app.route('/')
def whatever():
    return render_template('home.html', )

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

@app.route('/calendar')
def display():
    today = datetime.date.today().strftime("%Y-%m-%d")
    db = shelve.open('db','c')
    message = db.get(today, 'No Message for Today')
    db.close()
    return render_template('calendar.html', today = today, message = message)
@app.route('/add',methods = ["GET","POST"])
def add_message():
    if request.method == 'POST': #get data from server
        date = request.form.get('date')
    message = request.form.get('message')     #get date & message from form
    db = shelve.open('db','c')
    db[date] = message
    db.close()
    flash(f'Message added/updated for {date}.')  #user feedback but not working
    return redirect(url_for('home'))
@app.route('/delete/<date>')
def delete_message(date):
    db = shelve.open('db','c')
    if date in db:
        del db[date]
        flash('Message deleted.')
    else:
        flash('no message found for this date.')
    return redirect(url_for('calendar'))



if __name__ == '__main__':
    app.run(debug=True)