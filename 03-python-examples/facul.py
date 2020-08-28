def facul(number):
  result = 1
  for i in range(1,number+1):
    result = i * result
  return result

print(facul(4))
print(1*2*3*4)