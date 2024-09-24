def solution(id_pw, db):
    id = id_pw[0]
    pw = id_pw[1]
    for account in db:
        if account[0] == id:
            if account[1] == pw:
                return "login"
            else:
                return "wrong pw"
    return "fail"
