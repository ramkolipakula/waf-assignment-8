from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of students
student_records = [
    {"roll_no": "101", "name": "Alice Johnson", "department": "CSE"},
    {"roll_no": "102", "name": "Bob Williams", "department": "ECE"}
]

@app.route("/")
def home():
    return render_template("index.html", students=student_records)

@app.route("/register", methods=["POST"])
def register():
    roll_no = request.form.get("roll_no")
    name = request.form.get("name")
    department = request.form.get("department")
    if roll_no and name and department:
        student_records.append({"roll_no": roll_no, "name": name, "department": department})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
