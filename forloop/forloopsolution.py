result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count: ",count)


# 2. Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)


month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = int(input("Enter expense amount: "))
month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')

###########
for i in range(5):
    print(f"You ran {i+1} miles") # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")


############
for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)
