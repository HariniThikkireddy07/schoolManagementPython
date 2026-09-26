from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/students")
def students():
    students = [
        {"id": 101, "name": "Rahul Kumar", "class": "10th", "section": "A", "marks": 89},
        {"id": 102, "name": "Priya Sharma", "class": "10th", "section": "B", "marks": 94},
        {"id": 103, "name": "Arjun Reddy", "class": "9th", "section": "A", "marks": 82},
        {"id": 104, "name": "Sneha Rao", "class": "9th", "section": "B", "marks": 91},
        {"id": 105, "name": "Vikram Singh", "class": "8th", "section": "A", "marks": 78}
    ]

    return render_template("students.html", students=students)


@app.route("/teachers")
def teachers():
    teachers = [
        {"name": "Anita Sharma", "subject": "Mathematics", "experience": "8 Years"},
        {"name": "Ramesh Kumar", "subject": "Physics", "experience": "10 Years"},
        {"name": "Lakshmi Devi", "subject": "English", "experience": "6 Years"},
        {"name": "Suresh Reddy", "subject": "Computer Science", "experience": "7 Years"}
    ]

    return render_template("teachers.html", teachers=teachers)


@app.route("/courses")
def courses():
    courses = [
        {
            "name": "Mathematics",
            "description": "Algebra, Geometry, Trigonometry and Statistics",
            "students": 120
        },
        {
            "name": "Physics",
            "description": "Mechanics, Optics, Electricity and Modern Physics",
            "students": 95
        },
        {
            "name": "English",
            "description": "Grammar, Literature, Writing and Communication",
            "students": 110
        },
        {
            "name": "Computer Science",
            "description": "Programming, Databases and Web Development",
            "students": 85
        }
    ]

    return render_template("courses.html", courses=courses)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
