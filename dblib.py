import traceback
import pymysql
def get_db_details():
    dbdetails = {}
    dbdetails['MYSQL_HOST'] = "host.centerforinnovation.net"
    dbdetails['MYSQL_PORT'] = 3306
    dbdetails['MYSQL_USER'] = "tuser"
    dbdetails['MYSQL_PASS'] = "User.Tutorial"
    dbdetails['MYSQL_DB'] = "ptutorial"
    return dbdetails

def db_connection(dbdetails):
    connection = pymysql.connect(
        host=dbdetails['MYSQL_HOST'],
        port=dbdetails['MYSQL_PORT'],
        user=dbdetails['MYSQL_USER'],
        passwd=dbdetails['MYSQL_PASS'],
        db=dbdetails['MYSQL_DB']    
    )
    return connection

def add_user(userid,username,email):
    status = True
    try:
        dbdetails = get_db_details()
        conn = db_connection(dbdetails)
        with conn.cursor() as cur:
            query = """INSERT INTO srinivass_user(userid,username,email) VALUES(%s,%s,%s)"""
            cur.execute(query,(userid,username,email))
            conn.commit()
    except Exception as e:
        print("DB Error :", str(e))
        print("Error Data :", query,userid,username,email)
        print(traceback.format_exc)     
        status = False   
    finally:    
        conn.close()    
    return(status)        

def search_id(userid):
    try:
        dbdetails = get_db_details()
        conn = db_connection(dbdetails)
        with conn.cursor() as cur:
            query = """SELECT * FROM srinivass_user WHERE userid = '%s'"""
            cur.execute(query,(userid,))
            user_data = cur.fetchone()
    except Exception as e:
        print("DB Error :", str(e))
        print("Error Data :", query,userid)
        print(traceback.format_exc)          
    finally:
        conn.close()    
    return user_data

