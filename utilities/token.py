"""
private file ?
token a utilisé pour se connecter à l'api
"""

TOKEN = "449928d774153132c2c3509647e3d23f8e168fb50660fa27dd33c8342735b166"

def token(token_recu):
    if token_recu == TOKEN:
        return True
    return False
