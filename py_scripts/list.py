testList = ["potato", "carrot", "cabbage", "tomato", "brocoly", "ass"]
#				0 		1		 	2  		  3  		 4    	  5
testList1 = ["orange", "appel", "pear", True, 1, 2, 3, True, False]	# lista może składać się ze wszystkiego
print(f"eat healthy {testList}")
strList = testList.copy()	# kopiuje listę do innych list
strList = list(testList)	# kopiuje listę do innych list
amount = len(testList)
print(f"amount of healthy stuff = {amount}")

print(type(testList))#	ilość elementów w liście

for i in range(amount):
	print(testList[i])	#	pokazuje element listy na [i] pozycji 0-niskonczonoś
print(testList[-1])	# 	pokazuje ostani element listy
print(testList[3:5])	#	pokazuje elementy w zakresie 3:5 czyli elementy 3 i 4
print(testList[:4])	#	pokazuje elementy w zakresie od początku do 4 czyli 0
print(testList[5:])	#	pokazuje elementy w zakresie od 5 pozycji do końca

testList[0] = "patata" # nadpisuje element listy print(testList)
testList.insert(4, "salad")	# wpycha na pozycję 4 element przesówając każde kolejne o jedną pozycję na liście
print(testList)

testList.append("watermelon")	#	dopisuje na ostatnim miejscu nowy element listy
print(testList)

testList.extend(testList1)	#	dodaje do testList testList1
print(testList)

#	usówa elementy listy
testList.remove("appel")	#	po wartoścki, jeżeli się powtażają to usówa pierwszy element jaki jest
testList.remove(True)	#	po wartoścki, jeżeli się powtażają to usówa pierwszy element jaki jest
testList.pop(1)	#	po indexie
del testList[0]	#	po indexie
print(testList)

strList.sort() #	sortuje listę !!!tylko str bez int lub bool!!!
print(strList)


testList.clear() #	czyści listę
del testList #	usówa całkowicie listę