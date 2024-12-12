def prime(a):
  for i in range(2,a//2+1):
    if a % i == 0:
      return 'Не простое'
  return 'Простое'