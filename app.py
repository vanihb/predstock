from flask import Flask,render_template,request
import joblib

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('pre.html')

@app.route('/prediction1',methods = ['POST','GET'])
def prediction1():
    a = []
    if request.method == "POST":
        date = (request.form['date'])
        pclose = (request.form['pclose'])
        open = (request.form['open'])
        high = (request.form['high'])
        low = (request.form['low'])
        last = (request.form['last'])
        close = (request.form['close'])
        a.extend([date,pclose,open,high,low,last,close])
        model = joblib.load("dtrmodel.pkl")
        y_pred = model.predict([a])
        return render_template('pre.html',msg = "done",op=y_pred)
    return render_template("pre.html")




if __name__ == '_main_':
    app.secret_key = "vee"
    app.run(debug=True)