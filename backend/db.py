import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import typing

cred = credentials.Certificate("accountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'users')

def add_user(name: str, email: str, password: str, city: str, sports: list, age: int, gender: typing.Literal["Male", "Female"], phone: int) -> bool:
    try:
        doc_ref = users_ref.document(email)
        doc_ref.set({
            u'name': name,
            u'password': password,
            u'city': city,
            u'sports': " ".join(sports),
            u'age': age,
            u'gender': gender,
            u'phone': phone
        })
        return True
    except:
        return False

def get_user(email):
    doc_ref = users_ref.document(email)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def update_user(email: str, name: str, password: str, city: str, sports: list, age: int, gender: typing.Literal["Male", "Female"], phone: int) -> bool:
    try:
        doc_ref = users_ref.document(email)
        doc_ref.update({
            u'name': name,
            u'password': password,
            u'city': city,
            u'sports': " ".join(sports),
            u'age': age,
            u'gender': gender,
            u'phone': phone
        })
        return True
    except:
        return False

def delete_user(email):
    doc_ref = users_ref.document(email)
    doc_ref.delete()