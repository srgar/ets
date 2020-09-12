from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def univers_root():
    return render_template('index.html')

@app.route('/<string:page_name>')
def univers_all(page_name):
    return render_template(page_name)

def write_to_file(datax):
    with open('database.txt', mode='a') as database:
        eml = datax['email']
        subj = datax['subject']
        msg = datax['message']
        file = database.write(f'\n{eml},{subj},{msg}')

def write_to_csv(datacsv):
    with open('database.csv', mode='a', newline='') as dbscsv:
        eml = datacsv['email']
        subj = datacsv['subject']
        msg = datacsv['message']
        csv_writer = csv.writer(dbscsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([eml,subj,msg])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_frm( ):
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not saved to database File'
    else:
        return 'Something went wrong'