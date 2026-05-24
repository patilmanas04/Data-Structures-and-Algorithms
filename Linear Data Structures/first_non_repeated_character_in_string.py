string = "a green apple"

characterMap = dict()

for char in string:
    if char in characterMap:
        characterMap[char] += 1
    else:
        characterMap[char] = 1

print(characterMap)

for char in string:
    if characterMap[char] == 1:
        print(f"First non repeating character: {char}")
        break
