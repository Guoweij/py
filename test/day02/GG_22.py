dict1 = {
    "name": "GG",
    "age": 18,
    "height": 172,
    "hobby": "eat"

}
for a in dict1:
    print(a)

for b in dict1.keys():
    print(b)
print("-" * 30)
for c in dict1.values():
    print(c)
print("-" * 30)
for d, e in dict1.items():
    print(d, e)
