s = "this is some string"

# Build counter dictionary
# result = dict()
# for i in s:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1

# print(result)

# Find most common element
# count = 0
# for i in s:
#     i_count = s.count(i)
#     if i_count > count:
#         count = i_count

# print(count)


import collections

# Build counter dictionary
result = collections.Counter(s)
print(result)

# Find most common element
most_common = result.most_common(3)
print(most_common)









import collections
from typing import NamedTuple


# defaultdict
"""Group students and grades"""
def group_students(grades):
    student_grades = collections.defaultdict(list)
    for name, grade in grades:
        student_grades[name].append(grade)
    return student_grades.items()

"""same as above - setdefault"""
for name, grade in grades:
    student_grades.setdefault(name, list()).append(grade)

"""same as above"""
for name, grade in grades:
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

# grades = [("elliot", 91), ("neelam", 98), ("bianca", 81), ("elliot", 88)]
# print(group_students(grades))


"""Given an array of strings, group anagrams together."""
def group_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        anagrams[tuple(sorted(string))].append(string)
    return anagrams.values()

# strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(strings))


# Counter
words = "if there was there was but if there was not there was not".split()
counts = collections.Counter(words)
counts
counts.update(lst)
counts.most_common(2)
counts.element()
counts.subtract()

"""Default count for new key is 0"""
counts = collections.Counter()
counts["a"] += 1


# namedtuple
Student = collections.namedtuple("Student", ["fname", "lname", "age"])
s1 = Student("John", "Clarke", "13")
s1.fname

"""Using NamedTuple from typing module"""
from typing import NamedTuple

class Student(NamedTuple):
    fname: str
    lname: str
    age: str

s1 = Student("John", "Clarke", "13")
s1.fname


# deque
stack = collections.deque()
stack.append("a")
stack.extend("bcd")
stack.pop()

queue = collections.deque()
queue.appendleft("a")
queue.extendleft("bcd")
queue.pop()

deq.rotate(1)
deq.rotate(-1)
deq.popleft()
deq.clear()


# ChainMap
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "b": 4}
chain_map = collections.ChainMap(dict1, dict2)
chain_map.maps

child_dict = {"d": 5}
new_chain_map = chain_map.new_child(child_dict)
new_chain_map.maps
new_chain_map.parents
