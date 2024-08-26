from flask import Flask, session
app=Flask(__name__)

app.secret_key='nv0876'

@app.route('/')
def name():
    session
    return("hello")

if(__name__=="__main__"):
    app.run(debug=True,host='0.0.0.0')

