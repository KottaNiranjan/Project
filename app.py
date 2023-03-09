from flask import Flask,render_template,request,redirect
import numpy as np
import pickle
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy import text

db_string="mysql+pymysql://0abzlz1u7iugearjwgox:pscale_pw_BP9AafeM4BIihYL2LQIvdcSkoB2wJSotrTJHVx8RXRu@ap-south.connect.psdb.cloud/niranjan?charset=utf8mb4"




app=Flask(__name__)

model = pickle.load(open('Kidney.pkl', 'rb'))
try:
    engine = create_engine(db_string,
                    connect_args={
                        "ssl":{
                            "ssl-ca": "/etc/ssl/cert.pem"
                        }
                    })
    
except:
    result=[{'id': 1, 'username': 'niranjan', 'pass': 'Niranjan@8822', 'email': 'kottaniranjan8822@gmail.com'}, {'id': 2, 'username': 'mani', 'pass': 'mani@123', 'email': 'mani123@gmail.com'}, {'id': 3, 'username': 'yaseen', 'pass': 'yaseen@123', 'email': 'yaseen@gmail.com'}, {'id': 4, 'username': 'manoj', 'pass': 'manoj0311', 'email': 'manoj@gmail.com'}]

result=result=[{'id': 1, 'username': 'niranjan', 'pass': 'Niranjan@8822', 'email': 'kottaniranjan8822@gmail.com'}, {'id': 2, 'username': 'mani', 'pass': 'mani@123', 'email': 'mani123@gmail.com'}, {'id': 3, 'username': 'yaseen', 'pass': 'yaseen@123', 'email': 'yaseen@gmail.com'}, {'id': 4, 'username': 'manoj', 'pass': 'manoj0311', 'email': 'manoj@gmail.com'}]

@app.route("/")
def ro():
    return render_template("main.html")





@app.route("/register")
def load_login():
    return render_template("register.html")

@app.route("/register_validator",methods=["POST"])
def valid():
    engine = create_engine(db_string,
                    connect_args={
                        "ssl":{
                            "ssl-ca": "/etc/ssl/cert.pem"
                        }
                    })
    user=request.form["user"]
    email=request.form["email"]
    pas=request.form["pass"]
    repas=request.form["repass"]
    with engine.connect() as conn:
        result = conn.execute(text("select * from login"))
    result_dict=[]
    for row in result.all():
        result_dict.append(row._asdict())
    for i in result_dict:
        if i["username"]==user:
            return render_template("register.html",s="Username already Exists!!")
    if pas!=repas:
        return render_template("register.html",s="Passwords didnot match  Try Again!!")
    try:
        with engine.connect().execution_options(autocommit=True) as conn:
            query=text("INSERT INTO login(username,pass,email) VALUES (:username,:pass1,:email)")
            conn.execute(query,{"username":{user},"pass1":{pas},"email":{repas}})
            return render_template("register.html",s="Registerd Succesfully!!")
    except:
        result.append({"id":{len(result)+1},"username":{user},'pass':{pas},"email":{email}})
        return render_template("register.html",s="Registerd Succesfully!!")
        


@app.route("/login")
def log():
    return render_template("login.html")


@app.route("/login_validator",methods=['POST'])
def getvalue():
    login=[]
    us=request.form['user']
    pa=request.form["pass"]
    engine = create_engine(db_string,
                    connect_args={
                        "ssl":{
                            "ssl-ca": "/etc/ssl/cert.pem"
                        }
                    })
    try:
        with engine.connect() as conn:
            result1 = conn.execute(text("select * from login"))
            for row in result1.all():
                login.append(row._asdict())
    except:
        login=result
        return render_template("index.html",us=us)

    
    for i in login:
        if us=='admin':
            return render_template("administrator.html",login=login)
        if i['username']==us:
            if i['pass']==pa:
                email=i["email"]
                return render_template("index.html",us=us.upper(),email=email,pa=pa)
            else:
                return render_template("login.html",s="Invalid Password!!")
    return render_template("login.html",s="Invalid Login Details!!")



@app.route("/index")
def ind():
    return render_template("index.html")


@app.route("/index_validator",methods=["POST"])
def predict():
    if request.method=="POST":
        sg = float(request.form['sg'])
        htn = float(request.form['htn'])
        hemo = float(request.form['hemo'])
        dm = float(request.form['dm'])
        al = float(request.form['al'])
        appet = float(request.form['appet'])
        rc = float(request.form['rc'])
        pc = float(request.form['pc'])

        values = np.array([[sg, htn, hemo, dm, al, appet, rc, pc]])
        prediction = model.predict(values)

        return render_template('result.html', prediction=prediction)
    else:
        return render_template('index.html')

# @app.route("/")
# def load_login():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from login"))
#         login=[]
#         for row in result.all():
#             login.append(row._asdict())
#     return render_template("adminstrator.html",login=login)





# app.route("/api/helo")
# def g():
#     return "Hello"


# def hell():
#     return render_template("result.html")
try:
    if __name__=="__main__":
        app.run(debug=True)
except:
    pass