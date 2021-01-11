from dbconnectprgm.dbconnet import *
db=get_connection()
cursor=db.cursor()

sql="insert into faculty(id,name,subject)values('101','vijay','web prg')"

try:
    cursor.execute(sql)
    db.commit()
    print("inserted succesfully")
except Exception as e:
    print(e.args)
finally:
    db.close()