from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from datetime import timedelta

# import sqlite3	#<-- we won't need this anymore
from flask_sqlalchemy import SQLAlchemy #<-- this is an easier/safer way to do SQL back-end
from sqlalchemy import exc, func, desc

from demo_data import demoUsers, demoUserPhysicalStats, demoExercises, demoUserExercises, demoFeedbacks

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'CSCB20__1009161764__FitTracker'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 10)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fittracker.db'
db = SQLAlchemy(app)


################################
# Models
################################

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	user_type = db.Column(db.Integer)
	nickname = db.Column(db.String(255))
	
class UserPhysicalStats(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	height = db.Column(db.Float, nullable=False)
	body_weight = db.Column(db.Float, nullable=False)
	date_created = db.Column(db.String(255), nullable=False)

class Exercise(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	description = db.Column(db.Text, nullable=False)
	how_to_video = db.Column(db.String(255))

class UserExercise(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
	weight = db.Column(db.Float, nullable=False)
	reps = db.Column(db.Integer, nullable=False)
	sets = db.Column(db.Integer, nullable=False)
	date_created = db.Column(db.String(255), nullable=False)

class Feedback(db.Model):
	id = id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255))
	feedback = db.Column(db.String(255))

def create_user(email, password, user_type=0, nickname=None):
	user = User(email=email, password=password, user_type=user_type, nickname=nickname)
	db.session.add(user)
	db.session.commit()
	return user

def create_user_physical_stats(user_id, height, body_weight, date_created):
	physical_stats = UserPhysicalStats(user_id=user_id, height=height, body_weight=body_weight, date_created=date_created)
	db.session.add(physical_stats)
	db.session.commit()
	return physical_stats

def create_exercise(name, description, how_to_video=None):
	exercise = Exercise(name=name, description=description, how_to_video=how_to_video)
	db.session.add(exercise)
	db.session.commit()
	return exercise

def create_user_exercise(user_id, exercise_id, weight, reps, sets, date_created):
	user_exercise = UserExercise(user_id=user_id, exercise_id=exercise_id, weight=weight, reps=reps, sets=sets, date_created=date_created)
	db.session.add(user_exercise)
	db.session.commit()
	return user_exercise

def create_feedback(feedback, email=None):
	feedback = Feedback(email=email, feedback=feedback)
	db.session.add(feedback)
	db.session.commit()
	return feedback

def delete_user_exercise(user_exercise_id):
    user_exercise = UserExercise.query.get(user_exercise_id)
    if user_exercise:
        db.session.delete(user_exercise)
        db.session.commit()
        return True
    else:
        return False

def delete_user_stat(user_stat_id):
    user_stat = UserPhysicalStats.query.get(user_stat_id)
    if user_stat:
        db.session.delete(user_stat)
        db.session.commit()
        return True
    else:
        return False


#####################################################################
# Database setup & Populate some demos data if there are no records
# Updated from databae_setup.py
#####################################################################

with app.app_context():
	db.create_all()

	# Check if there are any records in the Users table
	num_records = User.query.count()
	if num_records == 0:
		users_data = demoUsers()
		for email, password, user_type, nickname in users_data:
			password_hashed = bcrypt.generate_password_hash(password)
			password_hashed_str = password_hashed.decode('utf-8')
			create_user(email, password_hashed_str, user_type, nickname)

	# Check if there are any records in the UserPhysicalStats table
	num_records = UserPhysicalStats.query.count()
	if num_records == 0:
		user_physical_stats_data = demoUserPhysicalStats()
		for user_id, height, body_weight, date_created in user_physical_stats_data:
			create_user_physical_stats(user_id, height, body_weight, date_created)

	# Check if there are any records in the Exercises table
	num_records = Exercise.query.count()
	if num_records == 0:
		exercises_data = demoExercises()
		for name, description, how_to_video in exercises_data:
			create_exercise(name, description, how_to_video)

	# Check if there are any records in the UserExercises table
	num_records = UserExercise.query.count()
	if num_records == 0:
		user_exercises_data = demoUserExercises()
		for user_id, exercise_id, weight, reps, sets, date_created in user_exercises_data:
			create_user_exercise(user_id, exercise_id, weight, reps, sets, date_created)

	num_records = Feedback.query.count()
	if num_records == 0:
		feedback_data = demoFeedbacks()
		for feedback, email in feedback_data:
			create_feedback(feedback, email)




################################
# Routes
################################

@app.route('/')
def home():
	exercises = Exercise.query.all()
	context = {
		"exercises": exercises
	}
	return render_template("home.html", **context)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact')
def contact():
		return render_template('contact.html')
	
@app.route('/api/contact', methods=['POST'])
def contacts():
	try:
		email = request.form['email']
		feedback = request.form['feedback']
		create_feedback(feedback, email)
		flash("Feedback successfully submitted", "success")
		return redirect(url_for('contact'))
	except exc.IntegrityError:
		flash("Error submitting feedback", "error")
		return render_template('contact')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if(request.method == "POST"):
		email = request.form['email']
		password = request.form['password']
		password_hashed = bcrypt.generate_password_hash(password)
		password_hashed_str = password_hashed.decode('utf-8')
		try:
			create_user(email, password_hashed_str)
			flash("User successfully added", "success")
			return redirect(url_for('login'))
		except exc.IntegrityError:
			flash("Username already exists", "error")
			return render_template('signup.html')
	elif "user" in session:
		return redirect(url_for('dashboard'))
	else:
		return render_template('signup.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
	if(request.method == "POST"):
		email = request.form['email']
		password = request.form['password']

		user = User.query.filter_by(email = email).first()
		if(not user):
			flash("No such user: " + email, "error")
			return render_template("login.html")
		elif(not bcrypt.check_password_hash(user.password, password)):
			flash("Sorry, wrong password", "error")
			return render_template("login.html")
		else:
			# Login successful, redirect to the dashboard page
			session['user'] = user.email
			session['user_type'] = user.user_type

			if (session['user_type'] == 1):
				return redirect(url_for('viewfeedback'))
			else:
				return redirect(url_for('dashboard'))
	elif "user" in session:
		return redirect(url_for('dashboard'))
	else:
		return render_template("login.html")
	

@app.route('/logout')
def logout():
	session.pop("user", None)
	session.pop("user_type", None)
	return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
	if("user" not in session):
		flash("must log in before you can access this page", "info")
		return redirect(url_for('login'))
	else:
		user = User.query.filter_by(email = session['user']).first()

		user_physical_stats = UserPhysicalStats.query.filter_by(user_id = user.id).order_by(UserPhysicalStats.date_created.desc()).all()

		user_exercises = UserExercise.query.filter_by(user_id = user.id).order_by(UserExercise.date_created.desc()).all()

		user_top_weights = db.session.query(UserExercise.exercise_id, Exercise.name, func.max(UserExercise.weight).label('max_weight')).\
			join(Exercise).\
			filter(UserExercise.user_id == user.id).\
			group_by(UserExercise.exercise_id, Exercise.name).\
			order_by(desc(func.max(UserExercise.weight))).all()
		
		if (len(user_physical_stats) > 0):
			body_weight_in_kg = user_physical_stats[0].body_weight
			body_height_in_m = user_physical_stats[0].height / 100
			bmi = body_weight_in_kg / (body_height_in_m * body_height_in_m)
			bmi = round(bmi, 2)
		else:
			bmi = 'N/A'

		context = {
			"user": user,
			"bmi": bmi,
			"total_activities": len(user_exercises),
			"user_physical_stats": user_physical_stats,
			"user_exercises": user_exercises,
			"user_top_weights": user_top_weights
		}
		return render_template("dashboard.html", **context)


@app.route('/personalstats')
def personalstats():
	if("user" not in session):
		flash("must log in before you can access this page", "info")
		return redirect(url_for('login'))
	else:
		user = User.query.filter_by(email = session['user']).first()
		user_physical_stats = UserPhysicalStats.query.filter_by(user_id = user.id).order_by(UserPhysicalStats.date_created.desc()).all()
		
		for stat in user_physical_stats:
			height_in_m = stat.height / 100
			stat.bmi = stat.body_weight / (height_in_m * height_in_m)
			stat.bmi = round(stat.bmi, 2)

		context = {
			"user": user,
			"user_physical_stats": user_physical_stats
		}
		return render_template("personalstats.html", **context)
	
@app.route('/api/personalstat', methods=['POST'])
def personalstat():
	try:
		user_id = request.form['user-id']
		height = request.form['height']
		body_weight = request.form['body-weight']
		date_created = request.form['date-created']
		create_user_physical_stats(user_id, height, body_weight, date_created)
		flash("Stats successfully added", "success")
		return redirect(url_for('personalstats'))
	except exc.IntegrityError:
		flash("Something went wrong", "error")
		return redirect(url_for('personalstats'))

@app.route('/activities')
def activities():
	if("user" not in session):
		flash("must log in before you can access this page", "info")
		return redirect(url_for('login'))
	else:
		user = User.query.filter_by(email = session['user']).first()

		user_exercises_history = db.session.query(UserExercise, Exercise.name)\
			.join(Exercise, UserExercise.exercise_id == Exercise.id)\
			.filter(UserExercise.user_id == user.id)\
			.order_by(desc(UserExercise.date_created))\
			.all()
		
		exercises = Exercise.query.all()

		context = {
			"user": user,
			"user_exercises_history": user_exercises_history,
			"exercises": exercises
		}
		return render_template("activities.html", **context)


@app.route('/api/activity', methods=['POST'])
def activity():
	try:
		user_id = request.form['user-id']
		exercise_id = request.form['exercise-id']
		exercise_weight = request.form['exercise-weight']
		exercise_reps = request.form['exercise-reps']
		exercise_sets = request.form['exercise-sets']
		exercise_date = request.form['exercise-date']
		create_user_exercise(user_id, exercise_id, exercise_weight, exercise_reps, exercise_sets, exercise_date)
		flash("Exercise successfully logged", "success")
		return redirect(url_for('activities'))
	except exc.IntegrityError:
		flash("Something went wrong", "error")
		return redirect(url_for('activities'))

@app.route('/rankings')
def rankings():
	if("user" not in session):
		flash("must log in before you can access this page", "info")
		return redirect(url_for('login'))
	else:
		user = User.query.filter_by(email = session['user']).first()
		bench_press_rankings = db.session.query(UserExercise, Exercise.name, User)\
			.join(Exercise, UserExercise.exercise_id == Exercise.id)\
			.join(User, UserExercise.user_id == User.id)\
			.filter(UserExercise.exercise_id == 1)\
			.order_by(desc(UserExercise.weight))\
			.limit(5)\
			.all()
		
		squat_rankings = db.session.query(UserExercise, Exercise.name, User)\
			.join(Exercise, UserExercise.exercise_id == Exercise.id)\
			.join(User, UserExercise.user_id == User.id)\
			.filter(UserExercise.exercise_id == 2)\
			.order_by(desc(UserExercise.weight))\
			.limit(5)\
			.all()
		
		deadlift_rankings = db.session.query(UserExercise, Exercise.name, User)\
			.join(Exercise, UserExercise.exercise_id == Exercise.id)\
			.join(User, UserExercise.user_id == User.id)\
			.filter(UserExercise.exercise_id == 3)\
			.order_by(desc(UserExercise.weight))\
			.limit(5)\
			.all()
		
		exercises = Exercise.query.all()

		context = {
			"user": user,
			"exercises": exercises,
			"bench_press_rankings": bench_press_rankings,
			"squat_rankings": squat_rankings,
			"deadlift_rankings": deadlift_rankings
		}
		return render_template("rankings.html", **context)
	
@app.route('/api/deleteactivity', methods=['POST'])
def deleteactivity():
	try:
		user_id = request.form['user-id']
		exercise_id = request.form['exercise-id']
		user = User.query.filter_by(email = session['user']).first()
		if (user.id != int(user_id)):
			flash("You are not authorized to delete this exercise", "error")
			return redirect(url_for('activities'))
		else:
			delete_user_exercise(exercise_id)
			flash("Exercise successfully deleted", "success")
			return redirect(url_for('activities'))
	except exc.IntegrityError:
		flash("Something went wrong", "error")
		return redirect(url_for('activities'))
	
@app.route('/api/deletepersonalstats', methods=['POST'])
def deletepersonalstats():
	try:
		user_id = request.form['user-id']
		stats_id = request.form['stat-id']
		user = User.query.filter_by(email = session['user']).first()
		if (user.id != int(user_id)):
			flash("You are not authorized to delete this personal stat", "error")
			return redirect(url_for('personalstats'))
		else:
			delete_user_stat(stats_id)
			flash("Personal Stat successfully deleted", "success")
			return redirect(url_for('personalstats'))
	except exc.IntegrityError:
		flash("Something went wrong", "error")
		return redirect(url_for('personalstats'))
	

@app.route('/profile', methods=['POST', 'GET'])
def profile():
	if("user" not in session):
		flash("must log in before you can access this page", "info")
		return redirect(url_for('login'))
	else:
		if (request.method == 'POST'):
			user = User.query.filter_by(email = session['user']).first()
			nickname = request.form['nickname']

			try:
				user.nickname = nickname
				db.session.commit()
				flash("Profile successfully updated", "success")
				return redirect(url_for('profile'))
			except exc.IntegrityError:
				flash("Something went wrong", "error")
				return redirect(url_for('profile'))
		else:
			return render_template("profile.html")

@app.route('/viewfeedback')
def viewfeedback():
	if(session['user_type'] == 1):

		feedbacks = Feedback.query.all()

		context = {
			"feedbacks": feedbacks
		}

		return render_template("viewfeedback.html", **context)
	else:
		flash("admin only", "info")
		return redirect(url_for('login'))
	
@app.route('/viewusers')
def viewusers():
	if(session['user_type'] == 1):

		admins = User.query\
		.filter(User.user_type==1)\
		.order_by((User.id))\
		.all()

		users = User.query\
		.filter(User.user_type==0)\
		.order_by((User.id))\
		.all()

		context = {
			"admins": admins,
			"users": users
		}
		return render_template("viewusers.html", **context)
	else:
		flash("admin only", "info")
		return redirect(url_for('login'))

app.run(host='0.0.0.0', port=82, debug=True)
