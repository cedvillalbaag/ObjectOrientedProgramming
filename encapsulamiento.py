class User:
    def __init__(self):
        self.email = input("Introduzca su email: ")
        # con guion bajo definimos un atributo como privado
        self.__password = input("Introduzca su contraseña: ")
        self.permissions = ["Edit", "Create", "Update"]
        self.username = None
    
    def set_username(self):
        self.username = input("Introduzca Username: ")
        print("Username actualizado a {}".format(self.username))

class UserPro(User):
    def __init__(self):
        super().__init__()
        self.permissions += ["Delete", "Download"]

    def pay_suscriptions(self, monto):
        print("Ud ha pagado exitosamente la suscripción {}".format(monto) )


class UserManager:
    
    def create_user(self, suscripcion):
        if suscripcion:
            user = UserPro()
        else:
            user = User()
        print("Se ha creado exitosamente su usuario. Sus permisos son: {}".format(user.permissions))

UserManager().create_user(False)