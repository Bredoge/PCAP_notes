dict = {	
#	<key>:<value>
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

print(dict)

x = dict.copy()	#	kopiuje słownik do innego słownika
print(x)

x.clear() #	czyści słownik
print(x)

a = dict.get("brand") #	gets the value of given key
print(a)

a = dict.items() #	daje wszyskie pary klucz:wartość
print(a)

dict["year"] = 2005	#	1 sposób nadpisywania donych w słowniku
dict["color"] = "white" #	również można urzywać by dodawać nowe elementy
print(dict)

a = dict.keys() #	daje wszystnie klucze ze słownika
print(a)
a = dict.values() #	daje wszystnie wartości ze słownika
print(a)

dict.pop("color") #	usówa parę(item) ze słownika, po kluczu
print(dict)

dict.popitem()	#	usówa ostatnio dodany element ze słownika
print(dict)

dict.update({"year":"2137"})	#	dodaje nową parę na końcu słownika
print(dict)