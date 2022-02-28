testTuple = ("apple", "pear", "orange", "banana", "cherry", 1, 22, 443, 200, True, False)	# krotka może składać się ze wszystkiego
#				0 		1		2  			3  		 4    	5	6	7	 8	  9		 10
one_element_tuple = ("element",)
print(testTuple)
print(type(one_element_tuple))

amount = len(testTuple)	#	ilość elementów w krotce
print(f"there is {amount} elements in tuple")

for i in range(amount):
	print(testTuple[i])	#	pokazuje element krotki na [i] pozycji 0-niskonczonoś
print(testTuple[-1])	# 	pokazuje ostani element krotki
print(testTuple[3:5])	#	pokazuje elementy w zakresie 3:5 czyli elementy 3 i 4
print(testTuple[:4])	#	pokazuje elementy w zakresie od początku do 4 czyli 0
print(testTuple[5:])	#	pokazuje elementy w zakresie od 5 pozycji do końca

#	!!!	do krotki nie można dopisywać nowych elementów ale są sposoby bo to zrobić	!!!

#	nadpisywanie elemenów poniżej
tmpList = list(testTuple)
tmpList[1] = "kiwi"
testTuple = tuple(tmpList)
print(testTuple)

#	dopisywanie elemenów poniżej
tmpList = list(testTuple)
tmpList.append("tea4two")
testTuple = tuple(tmpList)
print(testTuple)

(var0, var1, var2, *var3) = testTuple # nadawanie zmiennym (lub listom ostatni przykład) wartości z krotki (* oznacza że przypisać wszystkie pozostałe warości do listy ja będzei w środku to przyjmuje wszyskie wartości ale zostawia pojedyncze elementy dla pozostałych zmiennych)


print(f"\n{var0}\n{var1}\n{var2}\n{var3}")

enormous_tuple = testTuple + one_element_tuple # łączenie krotek
print(enormous_tuple)


del testTuple # usuwa krotkę