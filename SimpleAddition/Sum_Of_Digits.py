 def SumLoop(a):
  a = a.split(' ')

  return int(a[0])*int(a[1]) + int(a[2])

def SumDig(a):
  sum = 0
  i = 0
  while i < len(a):
    sum = sum + int(a[i])
    i+= 1
  return str(sum)

b = input()
c = []
for i in range(b):
  a = raw_input()
  c.append(SumDig(str(SumLoop(a))))
x = ' '.join(c)
print x
