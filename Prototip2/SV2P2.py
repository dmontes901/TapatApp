import newDades as dades
from newDades import User,Children,Taps,Statuses,Roles,Treatments
from flask import Flask, jsonify, request

'''for x in dades.users:
    print(x)

a= User(id=1, username="Kurl", password="12345", email="prova2@gmail.com")
print(a)'''

############  DAOs  ############

class UserDAO:
    def __init__(self):
        self.users = dades.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = dades.children

    def get_all_children(self):
        children_dicts = []
        for child in self.children:
            children_dicts.append(child.__dict__)
        return children_dicts

    def get_children_by_user_id(self, user_id):
        child_ids = []
        for rel in dades.relation_user_child:
            if rel["user_id"] == user_id:
                child_ids.append(rel["child_id"])
        children_dicts = []
        for child in self.children:
            if child.id in child_ids:
                children_dicts.append(child.__dict__)
        return children_dicts
