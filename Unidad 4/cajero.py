# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Generar un algoritmo de un cajero automático, este permite tres intentos para ingresar la
	# contraseña correcta, la contraseña debe ser igual a abcd, si se coloca la contraseña tres
	# veces incorrectamente el programa finaliza y manda un mensaje de error.
	# Cuando se ingresa la contraseña correcta entramos a un menú que permite tres opciones
	# ingresar saldo, retirar saldo, consultar saldo y salir del sistema.
	# La opción número 1 permite ingresar saldo a la cuenta, cuando se ingresa la cantidad a
	# depositar el sistema se actualiza y muestra la cantidad del saldo total y nuevamente
	# regresa al menú principal
	# La opción numero 2 permite retirar saldo de la cuenta, si el retiro supera la cantidad
	# de saldo en la cuenta, el sistema manda un mensaje de error, cuando se realiza un
	# retiro correcto el sistema regresa al menú principal y muestra el saldo total.
	# La opción número 3 muestra en pantalla el saldo total en la cuenta y retorna
	# nuevamente al menú principal.
	# La opción número 4, esta opción finaliza el sistema, cuando se escribe un número que
	# no se encuentra en el menú el sistema manda un mensaje de error indicando que esa
	# opción es incorrecta.
	balance = 2500
	contador = 0
	while contador<=2:
		print "Ingrese la contrasenia "
		contrasenia = raw_input()
		if contrasenia=="abcd":
			contador = 10
			while respuesta!=4:
				print "1- Ingresar saldo"
				print "2- Retirar Saldo"
				print "3- Verificar saldo"
				print "4- Salir"
				opcio = float(raw_input())
				if opcio==1:
					print "Cuanto dinero va a depositar"
					dineroingresado = float(raw_input())
					balance = balance+dineroingresado
					print "Tu saldo es de $ ",balance
				elif opcio==2:
					print "Cuanto dinero va a retirar"
					extraccion = float(raw_input())
					if extraccion>balance:
						print "Usted con cuenta con esa cantidad"
					else:
						balance = balance-extraccion
						print "su balance es de ",balance
				elif opcio==3:
					print "Tu saldo es de $ ",balance
		else:
			contador = contador+1
			if contador==10:
				print "Numero de intentos maximos alcanzado"
			else:
				print "Contrasenia incorrecta"

