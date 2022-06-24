from flask import Flask,request, url_for, redirect, render_template
import pickle
import sched, time
import pymongo
import numpy as np

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Minor"]
col = db["Minor"]
model=pickle.load(open('mode_1.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("index_1.html")
# s = sched.scheduler(time.time, time.sleep)
@app.route('/teams',methods=['POST','GET'])
def hello_teams():
    return render_template("team_contact.html")
@app.route('/predict',methods=['POST','GET'])
def predict():
    y = col.find()
    length=y.count()
    print(length)
    float_features1=[y[length-1]['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A0-ValueMid'],
                     y[length-1]['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A1-ValueMid'],
                     y[length-1]['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A2-ValueMid'],
                     y[length-1]['MAZAK_FZ:Servo load MAZAK_FZ P1 A0-ValueMid'],
                     y[length-1]['MAZAK_FZ:Servo load MAZAK_FZ P1 A1-ValueMid'],
                     y[length-1]['MAZAK_FZ:Servo load MAZAK_FZ P1 A2-ValueMid'],
                     y[length-1]['MAZAK_FZ:Servo load current(%) MAZAK_FZ P1 A0-ValueMid'],
                     y[length-1]['MAZAK_FZ:Servo load current(%) MAZAK_FZ P1 A1-ValueMid'],
                     y[length-1]['MAZAK_FZ:Servo load current(%) MAZAK_FZ P1 A2-ValueMid']]
    # float_features1=[y[0]['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A0-ValueMid'],
    #                  y[0]['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A1-ValueMid'],
    #                  y[0]['MAZAK_FZ:Speed of servo motor MAZAK_FZ P1 A2-ValueMid'],
    #                  y[0]['MAZAK_FZ:Servo load MAZAK_FZ P1 A0-ValueMid'],
    #                  y[0]['MAZAK_FZ:Servo load MAZAK_FZ P1 A1-ValueMid'],
    #                  y[0]['MAZAK_FZ:Servo load MAZAK_FZ P1 A2-ValueMid'],
    #                  y[0]['MAZAK_FZ:Servo load current(%) MAZAK_FZ P1 A0-ValueMid'],
    #                  y[0]['MAZAK_FZ:Servo load current(%) MAZAK_FZ P1 A1-ValueMid'],
    #                  y[0]['MAZAK_FZ:Servo load current(%) MAZAK_FZ P1 A2-ValueMid']]
    # float_features=[float(x) for x in request.form.values()]
    final=[np.array(float_features1)]
    print(y[0])
    print(float_features1)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('index_1.html',pred='Alert! Tool needs Replacement\n{}'.format('High'),bhai="kuch karna hain iska ab?")
    else:
        return render_template('index_1.html',pred='Tool is working fine.\n {}'.format('Low'),bhai="Your Forest is Safe for now")

if __name__ == '__main__':
    app.run(debug=True)
