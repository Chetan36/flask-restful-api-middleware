import user_repository

def add_user(req_json):
    return(user_repository.create(req_json))

def get_all_users():
    return(user_repository.find_all())
