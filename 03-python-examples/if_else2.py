def facul(number):
  result = 1
  for i in range(1,number+1):
    result = i * result
  return result

input = input("What should we calulate? ")
if input.isdigit() == False:
  print("Please type a number")
elif int(input) > 100:
  print("You need to buy the premium edition for this.")
else:
  print(facul(int(input)))