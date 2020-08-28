def facul(number):
  result = 1
  for i in range(1,number+1):
    result = i * result
  return result

input = input("What should we calulate?")
print(facul(int(input)))