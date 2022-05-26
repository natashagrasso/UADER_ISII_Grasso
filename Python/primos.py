import sys
import time
from textblob import TextBlob

if len(sys.argv) == 3:
    max = int(sys.argv[1])
    count = int(sys.argv[2])
else:
    print ("ERROR: Introdujo uno (1) o mas de dos (2) argumentos")
    print("SOLUCION: Introduce los argumentos correctamente")

#for loop for checking each number

eb1=TextBlob("Find primes up to what number?: ")
print(eb1.translate(from_lang ='in',to='it'),int(max)) #Traductor
primeList = []

for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList)
#-------------------------------------------------------------
# prime number calculator: find the first n primes

eb2=TextBlob("Find how many primes ?: ")
print(eb2.translate(from_lang ='in',to="it"), int(count)) #Traductor 
primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)

actual=time.strftime("%c")
print("Fecha y hora actual: "+actual)