hashMap = dict()

hashMap.update(name="Manas")
print(hashMap)

hashMap["enrollment_no"] = 202203103510235
print(hashMap)

hashMap.update({"branch": "B. Tech. CSE", "status": "Passed"})
print(hashMap)

print(f"Name: {hashMap.get('name')}")
print(f"Enrollment No: {hashMap.get('enrollment_no')}")
print(f"Year: {hashMap.get('year', 'Not applicable')}")
