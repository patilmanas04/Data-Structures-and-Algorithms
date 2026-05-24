string = "a green apple"

characterMap = dict()

for char in string:
    if char in characterMap:
        print(f"First repearted character: {char}")
        break
    else:
        characterMap[char] = 1
