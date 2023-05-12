from models.user import User as u
import database.Dao as databaseObj
import database.DaoConstants as DaoConst
from utils.loging import log
import hashlib


class UserHandle:
    def __init__(self):
        self.db = databaseObj.Dao()
        self.daoConst = DaoConst.DaoConstants()
        self.logger = log()

    def encodePass(self, password):
        encoded_pass = password.encode('utf-8')
        hashed_password = hashlib.sha256(encoded_pass).hexdigest()
        return hashed_password

    # Register working
    def createUser(self, u):
        try:
            alreadyExists = False
            alreadyExists = self.db.select_query(self.daoConst.GET_EXISTING_USER, (u.username, u.email))
            if not alreadyExists:
                hex_pass = self.encodePass(u.password)
                self.db.insertion_query(self.daoConst.CREATE_USER, (u.username, u.email, hex_pass))
                return True
            else:
                print("User already exists")
                return False
        except Exception as e:
            print(e)
            log.log_error(log, message="Unable to create user")
            return False

    # Login
    def loginUser(self, u):
        values = self.db.select_query(self.daoConst.GET_USER, (u.email))
        print('Mah values', values)
        my_tuple = values[0]
        username = my_tuple[0]
        stored_password = my_tuple[1]
        print('Stored pass is ', stored_password)
        if stored_password is not None and self.encodePass(u.password) == stored_password:
            print('Passwords Match')
            return username
        else:
            print('Passwords do not match wa wa wa')
            return None
