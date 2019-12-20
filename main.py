import math

use_you = input("Use 'you' (y/N)? ").lower() == "y"
if use_you:
  you = int(input("Use which number for 'you'? "))
def letter_to_spl(letter):
  if ord("a") <= ord(letter) and ord(letter) <= ord("h"):
    return "a " + "big " * (ord(letter) - ord("a")) + "cat"
  elif ord("i") <= ord(letter) and ord(letter) <= ord("p"):
    return "a " + "big " * (ord(letter) - ord("i")) + "pig"
  elif i == "u":
    return "you"
  elif i == "0":
    return "zero"
  else:
    return letter

def to_spl(code):
  code = code.replace("O", "")
  code = list(map(letter_to_spl,list(code)))
  return code

poss = list("0abcdefghijklmnopw+*23O");
if use_you:
  poss.append("u")
best = {}
soln = {}
for j in list(set(poss) - set(["+", "*", "O", "w", "2", "3"])):
  for k in list(set(poss) - set(["+", "*"])):
    for l in poss:
      for m in poss:
        for n in poss:
          for o in poss:
            for p in poss:
              stack = []
              cost = 0
              try:
                for i in j + k + l + m + n + o + p:
                  if i == "0":
                    stack.append(0)
                    cost += 4
                  elif ord(i) >= ord("a") and ord(i) <= ord("h"):
                    stack.append(2 ** (ord(i) - ord("a")))
                    cost += 5 + 4 * (ord(i) - ord("a"))
                  elif ord(i) >= ord("i") and ord(i) <= ord("p"):
                    stack.append(-(2 ** (ord(i) - ord("i"))))
                    cost += 5 + 4 * (ord(i) - ord("i"))
                  elif i == "w":
                    stack.append(2 * stack.pop())
                    cost += 6
                  elif i == "+":
                    stack.append(stack.pop() + stack.pop())
                    cost += 11
                  elif i == "*":
                    stack.append(stack.pop() * stack.pop())
                    cost += 15
                  elif i == "2":
                    stack.append(stack.pop() ** 2)
                    cost += 13
                  elif i == "3":
                    stack.append(stack.pop() ** 3)
                    cost += 11
                  elif i == "u":
                    stack.append(you)
                    cost += 3
              except Exception as err:
                1
                #print(err)
              else:
                #print("Code: " + j + k + l)
                #print("Stack: " + stack)
                #print("The cost was " + str(cost))
                if len(stack) == 1 and cost < best.get(stack[0], math.inf):
                  best[stack[0]] = cost
                  soln[stack[0]] = j + k + l + m + n + o + p
for s in sorted(best):
    print(str(s) + ": " + str(best[s]), soln[s], to_spl(soln[s]))
