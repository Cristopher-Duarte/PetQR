from AppPetQR.models import *
from django.contrib.auth.models import Permission, User



def Verificador(verificar, usuario):
    if(verificar == "USER" or verificar == "ADMIN" or verificar == "MEDICO"):
        user= usuario
        print(user)
        UserData = User.objects.all()
        if(len(UserData)>0):
            for userpk in UserData:
                captura = userpk.username
                print(captura)

                if(captura == str(usuario)):
                    return False
                
                    
            return True
        else:
            return True



