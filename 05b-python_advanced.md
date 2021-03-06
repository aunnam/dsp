## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> dict_items([('MD', 1), ('MA', 1), ('0', 1), ('MPH', 2), ('Ph.D.', 17), ('M.S.', 1), ('JD', 1), ('Ph.D', 5), ('PhD', 9), ('MS', 1), ('ScD', 2), ('Sc.D.', 4), ('B.S.Ed.', 1)])
 
>> The above shows 12 different degrees with their frequences, but some have written equivalent degrees such as 'Ph.D' meaning the same as 'PhD' and 'Ph.D.' in reality. So we can compile the results and fix variation to get the below result of 8 distinct degrees with 1 person having no degree whatsoever

>> dict_items([('MD', 1), ('MA', 1), ('0', 1), ('MPH', 2), ('PhD', 31), ('MS', 2), ('JD', 1), ('ScD', 6), ('B.S.Ed.', 1)])


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> Notably there is 1 'Assistant Professor is Biostatistics'. This is likely a typo and the 'is' was intended to be an 'of, so we will consider this a member of 'Assistant Professor of Biostatistics'. This means there are actually 3 distinct titles.

>> Associate Professor of Biostatistics: 12

>> Assistant Professor of Biostatistics: 13

>> Professor of Biostatistics: 13


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']



####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> There are 4 different email domains. The names of the email domains are below along with their frequencies. 

>> dict_items([('upenn.edu', 12), ('email.chop.edu', 1), ('cceb.med.upenn.edu', 1), ('mail.med.upenn.edu', 23)])

>> email.chop.edu is a unique email domain
>> cceb.med.upenn.edu is a unique email domain



Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:

>> Bilker [['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']]

>> Mitra [[' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu']]

>> Bryan [[' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']]


####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:

>> ('Jason', 'Roy') [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu']

>> ('Mingyao', 'Li') [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu']

>> ('Alisa', 'Stephens') [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu']

####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

>> ('Scarlett', 'Bellamy') [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']

>> ('Warren', 'Bilker') ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']

>> ('Matthew', 'Bryan') [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']


Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

