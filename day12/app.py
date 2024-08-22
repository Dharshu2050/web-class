#
from flask import Flask, render_template,request

app=Flask(__name__)

# @app.route('/')
# def name():
#     return render_template("index.html" , title="Hello world")

@app.route('/')
def home():
    return render_template("age.html")

@app.route('/sub', methods=['post'])
def submit():
    #2types requsest- get  panrathu  respones - request la iruka respones get panrathuku
    age=request.form['age']
    #string tha varum so we will convert into string into number
    age2=int(age)
    message=""
    if(age2<18):
        message="not eligible for voteing "
    else:
        message="eligible for vote"
        #left html irukarathu and right inga iruka mess get pana
    return render_template("index.html", message=message)

if(__name__=='__main__'):
    app.run(debug=True)
