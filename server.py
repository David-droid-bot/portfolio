#we are running the server and browser on the same computer
# and we give any other person this URL it won't work because it is working on local host
#so now we want to deploy our website online
#python anywhere allows us to host our files unto a server given to us for free
from flask import Flask, render_template,request,redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt',mode='a')as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a')as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
@app.route('/<string:page_name>')
def hello_world(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something is wrong'
