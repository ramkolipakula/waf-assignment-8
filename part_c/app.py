from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Available courses
COURSES = [
    {"code": "CS101", "title": "Web Application Frameworks", "credits": 4},
    {"code": "CS102", "title": "Database Management Systems", "credits": 3},
    {"code": "CS103", "title": "Operating Systems & Linux", "credits": 4},
    {"code": "CS104", "title": "Data Structures & Algorithms", "credits": 4}
]

# In-memory storage for registrations
registrations = [
    {"student_id": "STU001", "student_name": "Dev Sharma", "course_code": "CS101"},
    {"student_id": "STU002", "student_name": "Priya Patel", "course_code": "CS102"}
]

@app.route("/")
def index():
    return render_template("index.html", courses=COURSES, registrations=registrations)

@app.route("/register", methods=["POST"])
def register():
    student_id = request.form.get("student_id")
    student_name = request.form.get("student_name")
    course_code = request.form.get("course_code")

    if student_id and student_name and course_code:
        registrations.append({
            "student_id": student_id.strip(),
            "student_name": student_name.strip(),
            "course_code": course_code
        })
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5002)
# Added course limit logic placeholder
# Contributed by Collaborator: Added logging for registration events
