nomyapell = 0
altura = 0
peso = 0
masa = 0

nomyapell = input("Ingrese nombre y apellido: ")
altura = float(input("Ingrese altura: "))
peso = float(input("Ingrese peso: "))

masa = peso / (altura * altura)

if masa <= 15:
    print("Delgadez muy severa")
elif masa > 15 and masa  <= 15.9:
    print("Delgadez severa")
elif masa >= 16 and masa <= 18.4:
    print("Delgadez") 
elif masa >= 18.5 and masa <= 24.9:
    print("Peso Saludable")
elif masa >= 25 and masa <= 29.9:
    print("Sobrepeso") 
elif masa >= 30 and masa <= 34.9:
    print("Obesidad moderada") 
elif masa >= 35 and masa <= 39.9:
    print("Obesidad severa")  
elif masa >= 40:
    print("Obesidad muy severa")     


if masa <= 15:
    print("Delgadez muy severa")
else: 
    if  15.9 >= masa > 15:
        print("Delgadez severa")
    else:
        if 18.4 >= masa > 16:  
            print("Delgadez") 
        else:
            if 24.9 >= masa > 18.5:
                print("Peso Saludable") 
            else:
                if 29.9 >= masa > 25:
                    print("Sobrepeso")
                else:
                    if 34.9 >= masa > 30:
                     print("Obesidad moderada") 
                    else:
                        if 39.9 >= masa > 35:
                            print("Obesidad severa")
                        else:
                            if masa >= 40:
                                print("Obesidad muy severa")

