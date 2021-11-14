"""Prosta programka e napisana na latinica, dokazvaiki svoqta avtentichnost!
Slednata programa sama kalkulira dve proizvolni i izvurshva matematicheski deistviq na bazata na 4 funkcii s butonite ot 1 do 4 !
Priqtno testvane i do skoro! XD"""
 
number1 = float(input("Molq,vavedete purvata cifra >>> "))
number2 = float(input("Molq,vavedete vtorata cifra >>> "))
print(  """
                                    Menu

Kakvo jelaete da napravite?
Natisnete 1 za da suberete stoinostite.
Natisnete 2 za da izvadite stoinostite.
Natisnete 3 za da razdelite stoinostite.
Natisnete 4 za da umnojite stoinostite.
""" )
selection = int(input("Izberete vashata matematicheska funkcuq >>> "))
if selection == 1:
     result = number1 + number2
elif selection == 2:
    result = number1 - number2
elif selection == 3:
    result = number1 / number2
elif selection == 4:
    result = number1 * number2
else:
    result = "Greshka! Programata ne podurja vashata komanda!"

print(result)
input("Natisnete <ENTER> za izhod! Zapovqdaite otnovo!")
