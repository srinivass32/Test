import pymysql

def addtodb(userid,username,email):
    conn = pymysql.connect(
        host="host.centerforinnovation.net",
        port=3306,
        user="tuser",
        passwd="User.Tutorial",
        db="ptutorial"    
    )
    with conn:
        with conn.cursor() as cur:
            query = """INSERT INTO srinivass_user(userid,username,email) VALUES(%s,%s,%s)"""
            cur.execute(query,(userid,username,email))
            conn.commit()
    return(True)        

def searchbyid(userid):
    conn = pymysql.connect(
        host="host.centerforinnovation.net",
        port=3306,
        user="tuser",
        passwd="User.Tutorial",
        db="ptutorial"    
    )
    with conn:
        with conn.cursor() as cur:
            query = """SELECT * FROM srinivass_user WHERE userid = '%s'"""
            cur.execute(query,(userid,))
            x = cur.fetchone()
    return x

