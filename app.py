from flask import Flask,render_template,request,redirect
from main import openai_response
app = Flask(__name__)
print(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        dicton = openai_response(data['subject'])
        
        return render_template('index.html',dicton=dicton)
    
    else:
        return "sorry,something went wrong"
    


app.run(debug=True)