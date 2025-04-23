#Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
#Create a variable to store the string "Earth revolves around the sun"

    #Print "revolves" using slice operator
    #Print "sun" using negative index

##Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

street = "kasarani,Mwiki 00610"
city = "Nairobi"
country = "Kenya"
address = street + '\n' + city + '\n' + country
print("Address using + operator:",address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string:",address)

sentence='Earth revolves around the sun'
print(sentence[6:14])#output revolves 
print(sentence[-3:]) #output sun

num_fruits=10
num_veggies=5
print(f"I eat {num_veggies} veggies and {num_fruits} daily")

s='I eat 200 banana'
s=s.replace('banana','samosa')
s=s.replace('200','10')
print("Using two line replace:",s)

s='I eat 200 banana'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)
