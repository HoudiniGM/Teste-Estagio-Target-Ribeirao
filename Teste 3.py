#3) Descubra a lógica e complete o próximo elemento:

#a) 1, 3, 5, 7, ___
number = 1
print("a) ", end="")
for i in range(0, 5):
    print(number, end=" ")
    number += 2


#b) 2, 4, 8, 16, 32, 64, ____
number = 2
print("\nb) ", end="")
for i in range(0, 7):
    print(number, end=" ")
    number *= 2


#c) 0, 1, 4, 9, 16, 25, 36, ____
number = 0
increment = 1
print("\nc) ", end="")
for i in range(0, 8):
    print(number, end=" ")
    number += increment
    increment += 2


#d) 4, 16, 36, 64, ____
number = 4
print("\nd) ", end="")
for i in range(0, 5):
    print(int(number), end=" ")
    # Sucessor é igual a raiz quadrada do antecessor, +2, elevado ao quadrado
    number = ((number ** (1 / 2)) + 2) ** 2
    

#e) 1, 1, 2, 3, 5, 8, ____
previousNumber = 0
number = 1
print("\ne) ", end="")
for i in range(0, 7):
    print(number, end=" ")
    #O sucessor é sempre a soma dos dois antecessores, quando não há algum antecessor, acrescenta-se 0.
    nextPreviousNumber = number
    number += previousNumber
    previousNumber = nextPreviousNumber
    

#f) 2,10, 12, 16, 17, 18, 19, ____
print("\nf) Não soube resolver essa sequência.")
    
    
