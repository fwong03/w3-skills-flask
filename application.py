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
    jobs = {"software": "Software Engineer",
                "qa": "QA Engineer",
                "product": "Product Manager"
            }

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = int(request.form.get("salary"))
    job = jobs[request.form.get("job")]

    return "first name: %s, last name: %s, salary: %d, job: %s" % (firstname,
        lastname, salary, job)

    # return render_template("application-response.html",
    #                         fname=firstname, lname=lastname,
    #                         money=salary, position=job)


if __name__ == "__main__":
    app.run(debug=True)
