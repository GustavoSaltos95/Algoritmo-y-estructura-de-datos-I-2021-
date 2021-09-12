flag = True # este flag va a ser mi condicion de corte
while flag:
  contraseña = input("ingrese la contraseña: ")
  if contraseña =="1234":
    flag = False
    print("contraseña CORRECTA")
  else:
    print("contraseña incorrecta")