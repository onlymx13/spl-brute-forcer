import math
poss = list("0abcdefghijklmnop2+s3");
best = {}
for j in poss:
  for k in poss:
    for l in poss:
      stack = []
      cost = 0
      for i in j + k + l:
        try:
          if i == "0":
            stack.append(0)
            cost += 4
          elif ord(i) >= ord("a") and ord(i) <= ord("h"):
            stack.append(2 ** (ord(i) - ord("a")))
            cost += 5 + 4 * (ord(i) - ord("a"))
          elif ord(i) >= ord("i") and ord(i) <= ord("p"):
            stack.append(-(2 ** (ord(i) - ord("i"))))
            cost += 5 + 4 * (ord(i) - ord("i"))
          elif i == "2":
            stack.append(2 * stack.pop())
            cost += 6
          elif i == "+":
            stack.append(stack.pop() + stack.pop())
            cost += 11
          elif i == "s":
            stack.append(stack.pop() ** 2)
            cost += 13
          elif i == "3":
            stack.append(stack.pop() ** 3)
        except Exception as err:
          print(err)
          #print("cringe")
      #print("Code: " + j + k + l)
      #print("Stack: " + stack)
      #print("The cost was " + str(cost))
      if len(stack) == 1 and cost < best.get(stack[0], math.inf):
        best[stack[0]] = cost
        print("gamer")
for s in sorted(best):
  print(s, best[s])
