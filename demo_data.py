def demoUsers():
	return [
		('admin@fittracker.com', 'password', 1, 'admin'),
		('johndoe@example.com', 'password', 0, 'John Doe'),
		('janedoe@example.com', 'password', 0, 'Jane Doe'),
		('brianwilson@example.com', 'password', 0, 'Brian Wilson'),
		('sarahlee@example.com', 'password', 0, 'Sarah Lee'),
		('kevinmartin@example.com', 'password', 0, 'Kevin Martin'),
		('maryjones@example.com', 'password', 0, 'Mary Jones'),
		('michaelbrown@example.com', 'password', 0, 'Michael Brown'),
		('elizabethsmith@example.com', 'password', 0, 'Elizabeth Smith'), 
		('adamwang@example.com', 'password', 0, 'Adam Wang'),
		('laurawu@example.com', 'password', 0, 'Laura Wu'),
		('chris@example.com', 'password', 1, 'chris')
	]

def demoUserPhysicalStats():
	return [
		(2, 175, 75, '2023-01-30'),
		(2, 175, 74.5, '2023-02-07'),
		(2, 175, 74.2, '2023-02-25'),
		(2, 175, 74.6, '2023-03-17'),
		(2, 175, 74.1, '2023-03-28'),
		(3, 164, 64.8, '2023-01-25'),
		(3, 164, 64.5, '2023-02-05'),
		(3, 164, 63.8, '2023-02-13'),
		(3, 164, 63.5, '2023-03-01'),
		(3, 164, 63.0, '2023-03-15'),
		(4, 183, 82.5, '2023-01-30'),
		(4, 183, 82.6, '2023-02-07'),
		(4, 183, 82.3, '2023-02-25'),
		(4, 183, 81.8, '2023-03-17'),
		(4, 183, 82.1, '2023-03-28'),
		(5, 161, 55, '2023-01-30'),
		(5, 161, 54.5, '2023-02-07'),
		(5, 161, 54.2, '2023-02-25'),
		(5, 161, 54.6, '2023-03-17'),
		(5, 161, 54.1, '2023-03-28'),
		(6, 179, 78, '2023-01-30'),
		(6, 179, 78.5, '2023-02-07'),
		(6, 179, 78.2, '2023-02-25'),
		(6, 179, 78.6, '2023-03-17'),
		(6, 179, 78.1, '2023-03-28'),
		(7, 165, 75, '2023-01-30'),
		(7, 165, 74.5, '2023-02-07'),
		(7, 165, 74.2, '2023-02-25'),
		(7, 165, 74.6, '2023-03-17'),
		(7, 165, 74.1, '2023-03-28'),
		(8, 172, 77, '2023-01-30'),
		(8, 172, 77.5, '2023-02-07'),
		(8, 172, 77.2, '2023-02-25'),
		(8, 172, 77.6, '2023-03-17'),
		(8, 172, 77.1, '2023-03-28'),
		(9, 169, 72, '2023-01-30'),
		(9, 169, 72.5, '2023-02-07'),
		(9, 169, 72.2, '2023-02-25'),
		(9, 169, 72.6, '2023-03-17'),
		(9, 169, 72.1, '2023-03-28'),
		(10, 184, 85, '2023-01-30'),
		(10, 184, 84.5, '2023-02-07'),
		(10, 184, 84.2, '2023-02-25'),
		(10, 184, 84.6, '2023-03-17'),
		(10, 184, 84.1, '2023-03-28'),
		(11, 177, 95, '2023-01-30'),
		(11, 177, 94.5, '2023-02-07'),
		(11, 177, 94.2, '2023-02-25'),
		(11, 177, 94.6, '2023-03-17'),
		(11, 177, 94.1, '2023-03-28')
	]


def demoExercises():
	return [
		('Bench press', 'The bench press is a popular exercise for strengthening the chest, shoulders, and triceps muscles. The exercise involves lying on a bench and pushing a barbell or dumbbells away from the body, then lowering them to the chest in a controlled manner. Variations of the bench press can target different areas of the chest, such as the upper or lower chest, and can be performed with different equipment or weights.', 'https://youtube.com/embed/vcBig73ojpE'),
		('Squats', 'Squats are a compound exercise that work multiple muscle groups, including the legs, hips, and glutes. They are performed by standing with feet shoulder-width apart, lowering the body as if sitting down in a chair, and then standing back up again. Squats can be performed with different equipment, such as barbells, dumbbells, or bodyweight, and can be varied by changing the stance, depth, or speed of the movement.', 'https://youtube.com/embed/bEv6CCg2BC8'),
		('Deadlift', 'The deadlift is a strength exercise that works the lower body and back muscles. It involves lifting a barbell or dumbbells off the ground from a standing position, then lowering them back down with control. The exercise can be performed with different variations, such as the sumo or conventional deadlift, and can target different areas of the body, such as the hamstrings, glutes, or lower back. Proper form is important to avoid injury and get the most out of the exercise.', 'https://youtube.com/embed/VL5Ab0T07e4')
	]

def demoUserExercises():
	return [	
		(2, 1, 135.0, 10, 3, '2023-01-05'),
		(2, 2, 225.0, 5, 3, '2023-02-12'),
		(2, 3, 315.0, 3, 2, '2023-03-20'),
		(3, 1, 155.0, 8, 3, '2023-02-01'),
		(3, 2, 185.0, 6, 4, '2023-03-10'),
		(3, 3, 275.0, 4, 3, '2023-01-20'),
		(4, 1, 185.0, 6, 4, '2023-03-01'),
		(4, 2, 205.0, 5, 5, '2023-01-10'),
		(4, 3, 295.0, 3, 3, '2023-02-18'),
		(5, 1, 205.0, 6, 4, '2023-02-05'),
		(5, 2, 225.0, 5, 4, '2023-01-15'),
		(5, 3, 305.0, 3, 2, '2023-03-25'),
		(6, 1, 225.0, 5, 4, '2023-03-05'),
		(6, 2, 245.0, 4, 5, '2023-02-10'),
		(6, 3, 325.0, 2, 3, '2023-01-30'),
		(7, 1, 185.0, 6, 4, '2023-01-15'),
		(7, 2, 205.0, 5, 5, '2023-02-20'),
		(7, 3, 295.0, 3, 3, '2023-03-10'),
		(8, 1, 205.0, 6, 4, '2023-03-01'),
		(8, 2, 225.0, 5, 4, '2023-02-15'),
		(8, 3, 305.0, 3, 2, '2023-01-25'),
		(9, 1, 225.0, 5, 4, '2023-01-20'),
		(9, 2, 245.0, 4, 5, '2023-03-05'),
		(9, 3, 325.0, 2, 3, '2023-02-10'),
		(10, 1, 185.0, 6, 4, '2023-02-28'),
		(10, 2, 205.0, 5, 5, '2023-01-09'),
		(10, 3, 295.0, 3, 3, '2023-03-16'),
		(11, 1, 185.0, 6, 4, '2023-02-28'),
		(11, 2, 205.0, 5, 5, '2023-01-09'),
		(11, 3, 295.0, 3, 3, '2023-03-16')
	]

def demoFeedbacks():
	return [
		('good website', 'johndoe@example.com'),
		('bad website', ''),
		('good style', 'brianwilson@example.com'),
	]