def collatz_sequence(n):
  l = 0
  while n > 1:
    l += 1
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3 * n + 1
  return l


print(collatz_sequence(14))
