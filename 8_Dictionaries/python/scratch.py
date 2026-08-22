from DsDictionaryModule import DsDictionary

d = DsDictionary([("name", "Ada"), ("role", "Engineer")])
print(type(d))
print(d)

d["language"] = "Python"
print(d)

print("keys:", list(d.keys()))
print("values:", list(d.values()))
print("items:", list(d.items()))
