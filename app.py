from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    """
    this function is for writing the data inside the file and we can do that with open 
    """
    with open('database.txt', mode='a', encoding='utf-8') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    """
    this function is for writing the data that we get from the contact form
    into the csv file 
    """
    with open("database.csv", mode='a', newline='') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(file, delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    """
    this is function that get the data that is from the contact file and we pass those data to the 
    write_to_csv() for handling and writhing it inside the csv file
    """
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return "Some thing went wrong"
if __name__ == "__main__":
    app.run(debug=True)
