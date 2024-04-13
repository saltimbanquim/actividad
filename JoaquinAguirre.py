print (f"Bienvenido al mundo de la programación")
print (f"Para comenzar, ingresa tu nombre")

nom = input("")
print (f"  bienvenido  " + nom )
x = int(input("ingrese el valor de x para la siguente ecuacion (x**2+3x+1)/4 \n"))
ecuacion = ((x**2+3*x+1)/4)
print(ecuacion)

print (f"a continuacion entregue sus datos personales")
nombre = input("ingrese su nombre \n")
RUT = input("ingrese su rut \n")
Correo = input("ingrese su correo \n")
telefono = input("ingrese su telefono \n")

print(f'''
    NOMBRE:    {nombre}
    RUT:       {RUT}
    CORREO:    {Correo}
    TELEFONO:  {telefono}
      ''')