""" Job application Flask server.

Provides web interface for applying for a job.

"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""
    return render_template("index.html")

@app.route("/application-form")
def application_page():
    """Show application form page."""
    return render_template("application-form.html")


if __name__ == "__main__":
    app.run(debug=True)
