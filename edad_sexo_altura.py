sexo = 0
nombre = 0
edad = 0
altura = 0

sexo = input("sexo: ")
nombre = input("nombre: ")
edad = int(input("edad: "))
altura = float(input("altura: "))
               

   
if sexo == "masculino" and edad >= 18 and altura > 1.8:
    print("Es nayor de edad. Es un hombre alto")
else:
    if sexo == "femenino" and altura > 1.7:
        print("Es una mujer alta")
    else:
        print(nombre)
        
if sexo != "masculino" and sexo !="femenino" and edad < 18 and altura < 1.7:
    print(nombre)






     



    
    
