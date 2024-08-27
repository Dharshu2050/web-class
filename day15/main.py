from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route('/')
def name():
    return render_template('index.html')


@app.route('/login',methods=['post'])
def login():
    email=request.form['email']
    password=request.form['password']
    if(email=='dharshinieaswaran52@gmail.com' and password=='dashu25'):
        resp=redirect(url_for('das'))
        resp.set_cookie('nv','sdgregsdbd',max_age=5000)
        return resp
    return "email or password is wrong"

@app.route('/dashboard')
def das():
    value=request.cookies.get('nv')
    if(value=='sdgregsdbd'):
        return render_template('dashboard.html')
    return redirect(url_for('name'))

@app.route('/logout')
def logout():
    resp=redirect(url_for('name'))
    resp.set_cookie('nv','',max_age=0)
    return resp
    
if(__name__=='__main__'):
    app.run(debug=True)
