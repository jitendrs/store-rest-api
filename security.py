
from models.user import UserModel
from werkzeug.security import  safe_str_cmp



def authentication(username, password):
    user = UserModel.find_user_by_name(username)
    if user and safe_str_cmp(user.password,password):
        return user



def identity(payload):
    uid = payload['identity']
    return UserModel.find_by_id(uid)