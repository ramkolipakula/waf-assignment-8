from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for students
students = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "course": "Computer Science"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "course": "Information Technology"}
]

@app.route("/")
def index():
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name")
    email = request.form.get("email")
    course = request.form.get("course")
    if name and email and course:
        new_id = len(students) + 1
        students.append({"id": new_id, "name": name, "email": email, "course": course})
    return redirect(url_for("index"))

@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
# Added feature: Search module coming soon
