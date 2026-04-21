from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Your Azure API server URL from the previous assignment
api_url = "https://drew-peterson-salary-api-dpm-e3cchehwb0dagqh7.westus3-01.azurewebsites.net/predict"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Collect form values
    data = {
        "age": int(request.form["age"]),
        "gender": int(request.form["gender"]),
        "country": int(request.form["country"]),
        "highest_deg": int(request.form["highest_deg"]),
        "coding_exp": int(request.form["coding_exp"]),
        "title": int(request.form["title"]),
        "company_size": int(request.form["company_size"]),
    }

    # Send to Azure API
    response = requests.post(api_url, json=data)
    result = response.json()
    predicted_salary = result.get("predicted_salary", "Error retrieving prediction")

    # Format as currency
    if isinstance(predicted_salary, (int, float)):
        predicted_salary = f"${predicted_salary:,.2f}"

    return render_template("index.html", predicted_salary=predicted_salary)


if __name__ == "__main__":
    app.run(debug=True)
