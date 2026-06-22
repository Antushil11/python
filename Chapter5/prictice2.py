# You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert it into a set and print how many unique languages Divya knows.


programmingList=["Python", "Java", "C++", "Python", "Java", "C"]

print(type(programmingList))
#how to convert a list in to set

ProgrammingSet = set(programmingList)

print(type(ProgrammingSet))
print("divya Know languages ",len(ProgrammingSet))



