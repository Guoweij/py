str1 = "never mind  Don\'t  use too much PINYIN to code, try to use the english"
num = str1.find('use')
print(num)

num1 = str1.find("use", num + 1)
print(num1)
