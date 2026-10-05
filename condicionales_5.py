#Operadores and y or 

usuario_logueado = True
usuario_admin = False

if usuario_logueado or usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('acceso al sistema')
else:
    print('Debes inciar sesion')
