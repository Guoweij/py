func1=lambda a,b:a*b
print(func1(5, 6))

func2 =lambda x:x.get("age")
func3=lambda  d:d['age']
dict1 ={"name":"GG","age":21,"addres":"tutu"}
print(func2(dict1))
print(func3(dict1))