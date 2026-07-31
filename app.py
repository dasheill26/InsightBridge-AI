from flask import Flask, render_template, request
from services.company_analysis import analyze_company
from services.database import (
    initialize_database,
    save_analysis,
    get_all_analyses
)

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/company-analysis", methods=["GET", "POST"])
def company_analysis():

    result = None

    if request.method == "POST":

        company = request.form["company"]

        result = analyze_company(company)

        save_analysis(
            result["company"],
            result["overview"]
        )

    return render_template(
        "company_analysis.html",
        result=result
    )


@app.route("/history")
def history():

    analyses = get_all_analyses()

    return render_template(
        "history.html",
        analyses=analyses
    )


if __name__ == "__main__":
    app.run(debug=True)