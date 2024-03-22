def filter(func, seq):
   for item in seq:
      if func(item) == True:
          yield item

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
    print(x)

