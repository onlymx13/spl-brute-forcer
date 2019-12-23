import math, getopt, sys

args = sys.argv
argList = args[1:]
unixOptions = "hy:v"
gnuOptions = ["help", "you=", "verbose"]
try:
  arguments, values = getopt.getopt(argList, unixOptions, gnuOptions)
except getopt.error as err:
  print(err)
  sys.exit(2)

use_you = False

for currArg, currVal in arguments:
  if currArg in ("-h", "--help"):
      print("This is a program that brute forces different ways to write numbers in the Shakespeare Programming Language.\n")
      print("usage: python3 main.py [--help] [--you YOU] [--verbose]\n")
      print("optional arguments:")
      print("  -h, --help: Print this help and exit.")
      print("  -y YOU, --you YOU: Use a certain value as 'you'. If ommitted, no 'you' will be used. TODO: add 'I'.")
      print("  -v, --verbose: not currently supported.")
      exit()
  elif currArg in ("-y", "--you"):
    use_you = True
    you = currVal
    print("Using a value of %s as 'you'" % (currVal))
  elif currArg in ("-v", "--verbose"):
    print("Verbose mode not yet supported")

def letter_to_spl(letter):
  if letter == "0":
    return "zero"
  elif ord("a") <= ord(letter) and ord(letter) <= ord("h"):
    return "a " + "big " * (ord(letter) - ord("a")) + "cat "
  elif ord("i") <= ord(letter) and ord(letter) <= ord("p"):
    return "a " + "big " * (ord(letter) - ord("i")) + "pig "
  elif letter == "w":
    return "twice "
  elif letter == "+":
    return "the sum of"
  elif letter == "*":
    return "the product of"
  elif letter == "2":
    return "the square of"
  elif letter == "3":
    return "the cube of"
  elif letter == "u":
    return "you "
  else:
    return letter

def to_spl(code):
  code = code.replace("O", "")
  code = list(map(letter_to_spl,list(code)))
  code.reverse()
  return "".join(code)

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
            for p in list(set(poss) - set(list("0abcdefghijklmnop"))):
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
