import math
import re


iniciox = int(input("Cordenadas del expectador eje x: "))
inicioy = int(input("Cordenadas del expectador eje y: "))
targetx = int(input("Cordenadas del target eje x: "))
targety = int(input("Cordenadas del target eje y: "))
catetoa = abs(targetx - iniciox)
catetob = abs(targety - inicioy)
hipotenusa = math.sqrt((catetoa ** 2) + (catetob ** 2))
print("Cateto a: ", catetoa, "cateto b: ", catetob)
print("Hipotenusa: ", hipotenusa)
if (targetx - iniciox) < 0:
    angulo = 360 - (math.asin(catetob / hipotenusa) * (180.0 / math.pi))
elif (targety - inicioy) < 0:
    angulo = 180 - (math.asin(catetob / hipotenusa) * (180.0 / math.pi))
else: 
    angulo = math.asin(catetob / hipotenusa) * (180.0 / math.pi)
print("Angulo: ", angulo)

altura = int(input("Altura: "))
hipotenusa2 = math.sqrt((altura ** 2) + (hipotenusa ** 2))
if (targety - inicioy) < 0:
    angulo2 = 180 - (math.asin(altura / hipotenusa2) * (180.0 / math.pi))
else: 
    angulo2 = math.asin(altura / hipotenusa2) * (180.0 / math.pi)
print("Angulo 2: ", angulo2)