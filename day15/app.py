from flask import Flask,redirect
app=Flask(__name__)

app.secret_key='nv0876'

@app.route('/')
def name():
    
    return redirect("https://google.com")

@app.route('/test')
def test1():
    return "hello"


@app.route('/redirect')
def red():
    return redirect(url_for(test1))

@app.route('/cookies')
def cookies():
    # cookies will only work on request tym which means google poi url search panrathu ,cookies will only add in redirect
    response=redirect(url_for('test1'))
    response.set_cookie('dharshu','13456678',max_age=3600)
    return response

if(__name__=="__main__"):
    app.run(debug=True)