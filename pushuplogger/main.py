from flask import Blueprint, url_for, render_template, request, redirect, flash
from flask_login import login_required, current_user
from . import db
from .model import User
from .model import Workout


main = Blueprint("main", __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/logger')
@login_required
def logger():
    flash("status : True")
    user = User.query.filter_by(email=current_user.email).first_or_404()
    workout = user.workouts
    return render_template('allpushups.html', workout=workout)


@main.route('/new')
@login_required
def new_workouts():
    return render_template('newworkout.html', )

@main.route('/new', methods=['POST'])
@login_required
def workoutdetails():
    count = request.form.get('count')
    about = request.form.get('about')
    description = request.form.get('description')

    workout = Workout(count=count, works=about, description=description, author=current_user)
    db.session.add(workout)
    db.session.commit()
    
    return redirect('/logger')


@main.route('/workout/<int:workout_id>/update', methods=['GET','POST'])
@login_required
def update_workouts(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    if request.method == 'POST':
        workout.count = request.form['count']
        workout.works = request.form['about']
        workout.description = request.form['description']
        db.session.commit()

        return redirect('/logger')
    

    return render_template('update_works.html', workout = workout)


@main.route('/workout/<int:workout_id>/delete', methods=['GET'])
@login_required
def delete_workouts(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()

    return redirect('/logger') 