from flask import *
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)

def predictinginputdata(input_df):
    ct=pickle.load(open("coltransformer.pkl","rb"))
    lr=pickle.load(open("logmodel.pkl","rb"))
    x=ct.fit_transform(input_df)
    ans=lr.predict(x)[0]

    if ans==1:
        return "You will get job"
    else:
        return "You will not get job"

@app.route("/")

def displayform():
    return render_template("home.html")

@app.route("/reglink",method=['POST'])

def getinputdata():
    gender=request.form['Gender']
    sscmarks=float(request.form['sscmarks'])
    sscboard=request.form['sscboard']
    hscmarks=float(request.form['hscmarks'])
    hscboard=request.form['hscboard']
    subject=request.form['subject']
    degreemarks=float(request.form['degreemarks'])
    degree=request.form['degree']
    experience=request.form['experience']
    empmarks=float(request.form['empmarks'])
    Specialisation=request.form['Specialisation']
    mbamarks=float(request.form['mbamarks'])


    input_df=pd.DataFrame(data=[[gender,sscmarks,sscboard,hscmarks,hscboard,subject,
                                 degreemarks,degree,experience,empmarks,Specialisation,mbamarks]],columns=[])
    
    ans=predictinginputdata(input_df)
    return render_template("display.html",data=ans)

if(__name__):
    app.run(debug=True)


    
