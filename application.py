""" Job application Flask server.

Provides web interface for applying for a job.

"""


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index_page():
    """Show an index page."""
    return render_template("index.html")


@app.route("/application-form")
def application_page():
    """Show application form page."""
    return render_template("application-form.html")


@app.route("/application-response", methods=["POST"])
def application_confirmation():
    """Show application submission confirmation"""

    # Check if user entered a valid number for salary requirement.
    salary = request.form.get("salary")
    salary = salary.replace(',', '')

    try:
        salary = int(salary)
    except ValueError:
        return "Required salary must be a valid number. Press the back key to return."

    jobs = {"software": "Software Engineer",
            "qa": "QA Engineer",
            "product": "Product Manager"
            }

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    job = jobs[request.form.get("job")]
    salary = "{:,}".format(salary)

    return render_template("application-response.html",
                            fname=firstname, lname=lastname,
                            money=salary, position=job)


if __name__ == "__main__":
    app.run(debug=True)
