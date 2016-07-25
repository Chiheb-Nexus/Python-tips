#
# Some useful Python tips
#

"""
	Iteration
"""
# Exp 1
l = [1, 2, 3]
it = iter(l)
print(it.__next__()) # Or next(it). NB: Reaching the end of iteration will raise "StopIteration" exception
# Output : 1. The next call will be 2, then 3. Then if we call again our iterator we'll raise an exception

# Exp 2
l = [1, 2, 3]
for i in iter(l): # Or: for i in obj:
	print(i)
# Output: 1 2 3

# Exp 3
l = [1, 2, 3]
iterator = iter(l)
t = tuple(iterator) 
print(t) # output = (1, 2, 3) => output materialized as a tuple
# t = list(iterator) => output = [1, 2, 3] => output materialized as a list

# Exp 4
l = [1, 2, 3]
iterator = iter(l)
a, b, c = iterator
print(a,b,c) # output: 1 2 3
# print(a,b) # output: 1 2

# Exp 5
l = {"hi": 1, "hoo": 2}
for key in l:
	print(key) # output: hi ho => looking for dict keys

# Same with an iterator: Return dict keys
l = {"hi": 1, "hoo": 2}
iterator = iter(l)
print(iterator.__next__()) # output: hi
# print(next(iterator)) # output: hi

# Same: Return dict keys
l = {"hi": 1, "hoo": 2}
a, b = iter(l)
print(a, b) # output: hi hoo
# print(a) => output: hi

# Exp 6
l = [("Tunisia", "TN"), ("France", "FR")]
a = dict(iter(l)) # output: {'Tunisia': 'TN', 'France': 'FR'}

"""
	Generator expressions and list comprehensions
"""
# Exp 1
l = ["hi", "hoo", "humm"]
uppercase_iter = [k.upper() for k in l] # list comprehension
# uppercase_iter = (k.upper() for k in l) # output: ("HI", "HOO", "HUMM")
print(uppercase_iter) # output: ["HI", "HOO", "HUMM"]

# Same with lambda
l = ["hi", "hoo", "humm"]
func_lambda = lambda x: x.upper()
for i in l:
	func_lambda(i) # output: HI HOO HUMM

# Same with lambda
l = ["hi", "hoo", "humm"]
func_lambda = lambda x: x.upper()
my_list = [func_lambda(x) for x in l ] 
print(my_list) # output: ["HI", "HOO", "HUMM"]

# Exp 2
even_numbers = [x for x in range(11) if not x % 2] # output: [0, 2, 4, 6, 8, 10]
# odd_numbers = [x for x in range(11) if x % 2] # output: [1, 3, 5, 7, 9]

# Same
def is_even(n):
	return n % 2 

my_list = list(x for x in range(11) if not is_even(x)) # if 1: => if True / if 0: => if False
print(my_list) # output: [0, 2, 4, 6, 8, 10]

# Same with lambda
func_lambda = lambda x : x % 2
for i in range(11):
	if not func_lambda(i):
		print(i) # output: 0 2 4 6 8 10

# Same with lambda and Built-in functions
my_list = list(filter((lambda x: not x % 2), range(11)))
print(my_list) # output: [0, 2, 4, 6, 8, 10]

# Exp 3
match = "Team1 vs Team2"
seq = ('1', 'x', '2')
possible_results = [(match, y) for y in seq]
# output: [('Team1 vs Team2', '1'), ('Team1 vs Team2', 'x'), ('Team1 vs Team2', '2')]

# Same but more complex
matchs = ["Team1 vs team2", "Team1 vs team3", "Team2 vs Team3"]
seq = ('1', 'x', '2')
possible_results = [(x,y) for x in matchs for y in seq]
# output: [('Team1 vs team2', '1'), ('Team1 vs team2', 'x'), ('Team1 vs team2', '2'), ('Team1 vs team3', '1'),
# ('Team1 vs team3', 'x'), ('Team1 vs team3', '2'), ('Team2 vs Team3', '1'), ('Team2 vs Team3', 'x'), 
#('Team2 vs Team3', '2')]

# Exp 4
def generate_ints(n): # Generator
	for i in range(n):
		yield i

print(tuple(generate_ints(5))) # output: (0, 1, 2, 3, 4)
print(list(generate_ints(5))) # output: [0, 1, 2, 3, 4]

# Same 
def gen(n):
	for i in n:
		yield i # yield will often be returning None. Think about this case.

match = "Team1 vs Team2"
seq = ('1', 'x', '2')
possible_results = [(match, y) for y in gen(seq)]
# output: [('Team1 vs Team2', '1'), ('Team1 vs Team2', 'x'), ('Team1 vs Team2', '2')]

"""
	Built-in functions
"""
# Exp 1
def func_upper(s):
	return s.upper()

my_list = ["hi", "hoo", "humm"]
list_upper = list(map(func_upper, my_list ))
print(list_upper) # output: ['HI', 'HOO', 'HUMM']

# Same
my_list = ["hi", "hoo", "humm"]
list_upper = [x.upper for x in my_list] 
print(list_upper) # output: ['HI', 'HOO', 'HUMM']

# Same with lambda
my_list = ["hi", "hoo", "humm"]
func_lambda = lambda x: x.upper()
list_upper = [func_lambda(x) for x in my_list]
print(list_upper) # output: ['HI', 'HOO', 'HUMM']

# Exp 2
my_list = ["hi", "hoo", "humm"]
for i in enumerate(my_list):
	print(i)
# output: (0, 'hi') (1, 'hoo') (2, 'humm')

# Same
my_list = ["hi", "hoo", "humm"]
fin_out = list([x for x in zip(my_list, [x for x in range(len(my_list))])])
# output: (0, 'hi') (1, 'hoo') (2, 'humm')

"""
	itertools: COmbinatoric function
"""
import itertools
matchs = ["Team1", "Team2", "team3"]
comb = [x for x in itertools.combinations(matchs, 2)] # Group by 2
# output: [('Team1', 'Team2'), ('Team1', 'Team3'), ('Team2', 'Team3')]





