
from flask import Flask

app=Flask(__name__)


@app.route('/')


def home():
    return'dharshu'

@app.route('/dark')

def wel():
    return 'developer'

if __name__=="__main__":
    app.run(debug=true)

#cd change directry  routing url customize and next page link panrathu and button , debuging meaning work panitu irukom -start and stop athuvey panikom its me server start pani stop panum and once we can save the code it will be autometically start runing 