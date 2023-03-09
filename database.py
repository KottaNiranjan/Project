from sqlalchemy import create_engine
from sqlalchemy import text

db_string="mysql+pymysql://0abzlz1u7iugearjwgox:pscale_pw_BP9AafeM4BIihYL2LQIvdcSkoB2wJSotrTJHVx8RXRu@ap-south.connect.psdb.cloud/niranjan?charset=utf8mb4"

try:
    engine = create_engine(db_string,
                    connect_args={
                        "ssl":{
                            "ssl-ca": "/etc/ssl/cert.pem"
                        }
                    })

# with engine.connect() as conn:
    # result = conn.execute(text("select * from login"))
    # result_dict=[]
    # for row in result.all():
    #     result_dict.append(row._asdict())
    # query=text("INSERT INTO login(username,pass,email) VALUES (:username,:pass1,:email)")
    # conn.execute(query,{"username":"Kotta","pass1":"1234","email":"kotta@11234"})
    # result_dict=[]
    # for row in result.all():
    #     result_dict.append(row._asdict())
    # print(result_dict)
except:
    result=[{'id': 1, 'username': 'niranjan', 'pass': 'Niranjan@8822', 'email': 'kottaniranjan8822@gmail.com'}, {'id': 2, 'username': 'mani', 'pass': 'mani@123', 'email': 'mani123@gmail.com'}, {'id': 3, 'username': 'yaseen', 'pass': 'yaseen@123', 'email': 'yaseen@gmail.com'}, {'id': 4, 'username': 'manoj', 'pass': 'manoj0311', 'email': 'manoj@gmail.com'}]





