from flask import Flask, render_template ,request

app=Flask(__name__)

@app.route('/')
def home():
    return"<h1>helo</h1>"

@app.route('/html')
def ht():
    return render_template("index.html")

#dynamic url
@app.route('/dharshu/<names>')
def dynamic(names):
    return names

@app.route('/sub', methods=['POST'])
def sumbit():
    #form la irunthu get panrom demo 
    dmo=request.form['demo']
    return dmo

if __name__ =="__main__":
    app.run(debug=True)

#get request  -nedivil.in post requset -eg form submit