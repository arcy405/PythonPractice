# dict1 = {}
# n = set()
# print(type(n))

dict2 = {"good": "sth is great", "fetch": "to bring","1": "number one"}
marks = {"Harry": 56, "Pooja": 89, "Rita": 23, "Naina": 59, "Archana": "100"}
print(dict2["good"])
print(marks["Archana"])
print(marks["Rita"])
marks["Anish"] = "77"

print(marks)

print(marks.get("Pooja"))
print(marks.keys())
print(marks.values())
print(marks.items())