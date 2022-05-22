def aniobisiesto(anio):
    if anio%4==0 and (anio%100!=0 or anio%400==0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
dato= int(input("Ingrese un numero del año para determinar si es bisiesto o no:\n "))
aniobisiesto(dato)
