from flask import Flask, request

# import psycopg2

app = Flask(__name__)


@app.route("/")
def home():
    return open("form.html").read()


@app.route("/click", methods=["POST"])
def submit():

    name = request.form["name"]
    company = request.form["company"]
    rating = request.form["rating"]

    print(f'name is {name}')
    print(f'company is {company}')
    print(f'rating is {rating}')

    return {'name':name,'company':company,'rating':rating}

    
if __name__ == "__main__":
    app.run(debug=True)