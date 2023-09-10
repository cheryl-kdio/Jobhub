from abc import ABC,abstractmethod
from random import randint
from memory_id import Memory

class Utilisateur(ABC) :

        
    def create_account(self):
        id = randint(0,999999999999)
        while id in Memory.dicti :
            id = randint(0,999999999999)
        
        name_user=input('nom utilisateur :')
        password='a'
        password2='a'
        while password != password2:
            password=input("mot de passe :")
            password2=input("confirmation du mot de passe :")

        Memory.dicti.add_dict(id,[name_user,password])

crea = Utilisateur()
crea.create_account()


        


        

            
            
    