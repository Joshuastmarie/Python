# a cursor is the object we use to interact with the database
import pymysql.cursors
from werkzeug.utils import secure_filename
from copy import deepcopy
import os
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'rootroot', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
    
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 



    def query_db_blobs(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                print(data)
                data_copy = deepcopy_data(data)
                print("test")
                # binary_data = data['img_blob'].read()
                filename = secure_filename(data['img_blob'].filename)
                data['img_blob'].save(filename)
                # file_path = data['img_blob'].filename
                with open(filename, 'rb') as f:
                    binary_data = f.read()
                data_copy['img_blob'] = binary_data
                query = cursor.mogrify(query, data_copy)
                print("Running Query:", query)
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
    

        
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

def deepcopy_data(data):
    # Create a new FileStorage object using the same underlying file as the original
    new_file = open(data['img_blob'].filename, 'rb')
    new_filestorage = FileStorage(stream=new_file, filename=data['img_blob'].filename,
        content_type=data['img_blob'].content_type)
    # Copy the other data in the dictionary separately
    new_data = {
        'listing_id': data['listing_id'],
        'img_blob': new_filestorage
    }
    return new_data