from flask import Flask, render_template, request, redirect
from database import create_table, add_student, get_students, delete_student, get_student_by_id, update_student

app = Flask(__name__)

# I created a function for the code to create a table in the database if it doesn't exist
create_table()

# Route for the homepage
@app.route('/')
def index():
    students = get_students()
    return render_template('index.html', students=students)

#route to adding a new student to the database
@app.route('/add_student', methods=['POST'])
def add():
    name = request.form['name']
    matric_number = request.form['matric_number']
    department = request.form['department']
    add_student(name, matric_number, department)
    return redirect('/')

@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete(student_id):
    # The code below will delete the student with the specified ID from the database
    delete_student(student_id)
    # Redirect to the homepage after deleting the student
    return redirect('/')

#code to update the database
@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit(student_id):
    if request.method == 'GET':
        student = get_student_by_id(student_id)
        return render_template('edit_student.html', student=student)
    elif request.method == 'POST':
        name = request.form['name']
        matric_number = request.form['matric_number']
        department = request.form['department']
        update_student(student_id, name, matric_number, department)
        return redirect('/')

update_student(5, 'eric', 190591123, 'csc')


if __name__ == "__main__":
    app.run(debug=True)

