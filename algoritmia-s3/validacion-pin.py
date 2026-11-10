pin_correcto = 1234
intentos = 0
acceso_concedido = False

while intentos < 3 and not acceso_concedido:
    pin_ingresado = int(input(f"Digite su clave (Intento {intentos + 1} de 3): "))

    if pin_ingresado == pin_correcto:
        acceso_concedido = True
        print("¡Clave correcta! Bienvenido.")
    else:
        intentos += 1
        if intentos < 3:
            print("Clave errónea. Intente otra vez.")

if not acceso_concedido:
    print("Se agotaron los 3 intentos. Cuenta bloqueada.")