edad = int(input("Escribe tu edad: "))
terminos = input("¿Acepta los términos y condiciones? (S/N): ").upper()

if terminos != "S" and terminos != "N":
    print("Error: Ingrese un carácter válido para los términos y condiciones (S/N).")

elif edad < 14:
    print("Debes tener al menos 14 años para registrarte.")

elif terminos == "S":
    print("Registro exitoso.")

else:
    print("Debe aceptar los términos y condiciones para registrarse.")