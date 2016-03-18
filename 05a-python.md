# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples and both lists of values, but tuples are immutable meaning they cannot be changed, while lists can be changed. Tuples will work as keys to a dictionary while lists will not, simply because there is no valid hash method for lists.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets unlike lists have no order for their elements, dont allow duplicates, and requires its items to be hashable. 

>> x = [4,2,3,4,5,1]

>> y = Set([1,2,3,4,5,6])

>> Performance for finding an element within the structure is significantly faster on average in the set compared to the list. The reason for this is because sets are implemented with hashes so a lookup can be done in O(1) time.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an operator used to create an effective throwaway function to perform an operation without having to create a function for it.

>> f = lambda x, y : x + y

>> sorted(['S', 'b', 'B', 'M'], key=lambda word: word.upper())

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a concise way to create lists and is commonly used to create lists which can be made simply by doing certain operations to an input. 

>> squares = [x**2 for x in range(8)] ///prints the first 8 square numbers starting at 0 and ending at 49

>> foo = [1,2,3,4,5,6,7,8,9]

>> foomap = map(lambda x: x * 2, foo) // foomap is a list of doubled values from foo

>> foofilter = filter(lambda x: x % 2 == 0, foo) // foofilter is a list of all the even numbers from foo

>> Map runs a function on all elements passed in as input to the map. Filter checks whether each each element passed in as input returns true for the function provided to filter, and returns only the elements which returned true.

>> compset = {x for x in range(10) if x % 2 == 0} /// set comprehension of all the even numbers from 0 to 9

>> compdict = {key: val for key, val in enumerate([1,2,3,4,5,6]) if val%2==0} /// dict comprehension of all even numbers from 1 to 6


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





