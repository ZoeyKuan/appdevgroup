from flask import Blueprint, render_template
blueprint = Blueprint('blueprint_blueprint', __name__)
@blueprint.route('/<n>')
def h(n):
    return render_template('ind.html', content = n)
@blueprint.route('/boom')
def he():
    return 'boom'