# A tuple in Python is an immutable ordered collection of elements.  Can't update , add  and remove element

# Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
# Tuples can hold elements of different data types.
# The main characteristics of tuples are being ordered, heterogeneous and immutable.

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)

tup=("geeks") # treated as string
print(type(tup))

tup=("Geeks",) # treated as tuple
print(type(tup))

tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

# Concatenation of tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')

tup3 = tup1 + tup2
print(tup3)

# Slicing

tup = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])

# Deletion

#tup = (0, 1, 2, 3, 4)
#del tup

#print(tup)

# Unpacking with * Asterisk 

tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)

ytup=tuple((x for x in range(1,4)))
print(ytup)
# ytup.append(5)  # This will raise an AttributeError since tuples are immutable

print(type(ytup))

# k_nearest_labels = [label for _, label in distances[:k]]

# 2. Tuple Unpacking & The _ Convention: for _, label in ...
# Each element in distances is a 2-item tuple: (distance, label) (e.g., (1.2, "cat")).

# When iterating, Python unpacks the two elements:

# The first value (1.2) goes into _.

# The second value ("cat") goes into label.

# Why use an underscore _?

# In Python, _ is a standard naming convention for a variable you intentionally plan to ignore. We already sorted the list, so we no longer need the exact distance number—we only care about the label.


# Both are forms of unpacking, but they are used in different ways.

# In Python, there are two distinct concepts that go by the name "unpacking":

# 1. Standard (Positional) Unpacking — No * Needed
# When you know the exact number of elements in a tuple, you assign them directly by placing variables separated by commas on the left side of the assignment:

# Python
# Direct assignment
dist, label = (1.2, "cat")
# dist  -> 1.2
# label -> "cat"

# Inside a loop (exact same mechanism)
for dist, label in [(1.2, "cat"), (2.5, "dog")]:
    print(label)
# Because each tuple has exactly 2 items, Python automatically matches the 1st value to dist (or _) and the 2nd value to label.

# 2. When the Asterisk (*) IS Used for Unpacking
# The asterisk * (often called the splat or star operator) is used in two specific scenarios:

# A. Extended Unpacking (Catching the "Rest" of the Items)
# When you don't know the exact length of the tuple, or only want specific parts, * captures the remaining items into a list:

# Python
data = (1.2, "cat", "indoor", 4.5, "orange")

dist, label, *extra_info = data

print(dist)        # 1.2
print(label)       # "cat"
print(extra_info)  # ['indoor', 4.5, 'orange']
# B. Function Argument Unpacking
# When passing an entire tuple into a function where each item should become a separate positional argument:

# Python
def add(a, b):
    return a + b

point = (3, 5)

# Without *: add(point) -> TypeError (missing 1 argument)
# With *:
print(add(*point))  # Evaluates to add(3, 5) -> 8


# The Fundamental DifferenceConcept_ (Underscore)* (Asterisk / Splat)What is it?A valid variable name (by convention used for "I don't care about this").A syntax operator (for unpacking / grouping iterables).How many items does it hold?Exactly 1 item per _.0 or more items (collected into a list).Can it stand alone?Yes (_ = 10).No, it must prefix a variable name (e.g., *rest or *_).1. _ (Underscore): The 1-to-1 "Ignore" Variable_ is a real variable in Python—it just signals to humans and linters that the value won't be used.Example A: Throwing away 1 item in a fixed tuplePython# Fixed structure: exactly 3 items
record = ("Alice", 29, "Engineer")

name, _, job = record  # Ignore the age (index 1)

print(name)  # 'Alice'
print(job)   # 'Engineer'
# Example B: Throwing away values in a loopPython# Repeat an action 3 times without needing a loop counter
for _ in range(3):
    print("Hello!")
# Limitation of _ alone: It strictly demands a 1-to-1 match. If the tuple has 5 elements, writing a, _ = (1, 2, 3, 4, 5) will crash with ValueError: too many values to unpack.2. * (Asterisk): 
# The 1-to-Many "Collector" Operator* tells Python to collect all remaining or variable-length elements into a list.Example A: Catching the rest of the itemsPython
scores = [100, 95, 88, 72, 60]

# Extract the highest score, and keep all other scores in a list
top_score, *other_scores = scores

print(top_score)     # 100
print(other_scores)  # [95, 88, 72, 60]
# Example B: Grabbing the first and last itemsPython
log_entry = ("2026-08-15", "SERVER_1", "CPU_LOAD", "WARN", "DISK_FULL")

date, *middle_info, status = log_entry

print(date)         # '2026-08-15'
print(middle_info)  # ['SERVER_1', 'CPU_LOAD', 'WARN']
print(status)       # 'DISK_FULL'
# 3. The Power Combo: *_ (Ignore Multiple Items)When you combine both, *_ means: "Collect all the rest of the items into a list and ignore them entirely."Python
data = ("USD", 1.25, 1.28, 1.30, 1.27, "ACTIVE")

# We only care about the currency (first) and status (last)
currency, *_, status = data

print(currency)  # 'USD'
print(status)    # 'ACTIVE'
# Everything in between (regardless of whether there are 3 items or 100) is ignored!
# Side-by-Side Comparison in CodePython# Our sample tuple with 5 elements
sample = (10, 20, 30, 40, 50)

# -------------------------------------------------------------
# 1. Standard Unpacking with _ (Must match EXACT number of items)
# -------------------------------------------------------------
first, _, _, _, last = sample
print(first, last)  # 10, 50

# -------------------------------------------------------------
# 2. Asterisk Unpacking (Collects into a named list)
# -------------------------------------------------------------
first, *middle, last = sample
print(middle)  # [20, 30, 40]

# -------------------------------------------------------------
# 3. Combined *_ (Collects into a throwaway list)
# -------------------------------------------------------------
first, *_, last = sample
print(first, last)  # 10, 50