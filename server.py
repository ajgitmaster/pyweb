from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

@app.route('/<string:username>')
def main_route(username):
    return render_template('index.html', username=username)

@app.route('/submit_form', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('index.html', username=request.form['username'], submitted=True)
    else:
        return "Method not allowed"

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['name'], data['email'], data['message']])