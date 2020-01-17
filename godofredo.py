# Calculadora
ejecutar = 1


while ejecutar == 1:
	print("Este programa permite hacer una operación básica con dos números")
	print("Para realizar esto, es necesario que me indiques el tipo de operación que deseas:")
	print("1) Suma ")
	print("2) Resta ")
	print("3) Multiplicación ")
	print("4) División ")
	opcion = int(input("Dame la opción que deseas: "))
	primero = float(input("Dame el primer número a utilizar: "))
	segundo = float(input("Dame el segundo número: "))
	if opcion >= 1 or opcion <=4:
		if opcion == 1:
			resultado = primero + segundo
			print("El resultado es: ")
			print("%.2f"%resultado)
		elif opcion == 2:
			resultado = primero - segundo
			print("El resultado es: ")
			print("%.2f"%resultado)
		elif opcion == 3:
			resultado = primero * segundo
			print("El resultado es: ")
			print("%.2f"%resultado)
		elif opcion == 4:
			resultado = primero / segundo
			print("El resultado es: ")
			print("%.2f"%resultado)
		else:
			print("Error, opcion invalida")
	else:
		print("Opción invalida")
	ejecutar=int(input("¿Quieres volver a intentarlo? 1 = si / 2 = No"))