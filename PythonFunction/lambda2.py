def my(n):
  return lambda a : a * n
mydoubler = my(2)
print(mydoubler(11))