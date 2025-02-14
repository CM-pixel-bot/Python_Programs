Mobile = {
	"brand": "IPhone",
	"Model": "IOS13",
	"Screen Size" : 6.1
}
#calling key values
for key in Mobile:
	print(Mobile[key])
	
#calling values values
print("Here are the values")
for key in Mobile:
    print(Mobile[key])
    
#adding new element
Mobile["Color"] = "Black"

for values in Mobile.values():
    print(values)

for key,values in Mobile.items():
    print(key,values)
    
print(Mobile.values())
print(Mobile.keys())
print(Mobile.items())

if "Color" in Mobile:
    print("It's color is black")
else:
    print("It's color is not black")
