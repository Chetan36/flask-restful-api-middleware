import user_repository

def add_user(req_json):
    return(user_repository.create(req_json))

def get_all_users():
    return(user_repository.find_all())

def get_user_by_id(user_id):
    return(user_repository.find_by_id(user_id))

def update_user(user_id, req_json):
    return(user_repository.update(user_id, req_json))
