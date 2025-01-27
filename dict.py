students = {"Alice": 85, "Bob": 90, "Charlie": 78}

maxScore = max(students,key = students.get)

print(maxScore)

#*********************************************
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

#____________________________________________________
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 

#____________________________________________________

dict1 = {"Alice": 85}

dict2 = {"Bob": 90}

mergedDict = {**dict1, **dict2}
print(mergedDict)  # Output: {'Alice': 85, 'Bob': 90}


#____________________________________________________

string = "banana"
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1
print(freq)  # Output: {'b': 1, 'a': 3, 'n': 2}

#____________________________________________________

words = ["apple", "cat", "dog", "banana"]
grouped = {}
for word in words:
    length = len(word)
    grouped.setdefault(length, []).append(word)
print(grouped)  # Output: {5: ['apple'], 3: ['cat', 'dog'], 6: ['banana']}

#____________________________________________________
#nested dictonary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily['child1']['name'])
#________________________________________________________
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for key,obj in myfamily.items():
    print(key)
    
    for x in obj:
       print(f"obj-key: {x}------>obj-value: {obj[x]}")
       
       
"""
output

child1
obj-key: name------>obj-value: Emil
obj-key: year------>obj-value: 2004
child2
obj-key: name------>obj-value: Tobias
obj-key: year------>obj-value: 2007
child3
obj-key: name------>obj-value: Linus
obj-key: year------>obj-value: 2011
"""



