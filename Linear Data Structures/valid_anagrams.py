from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    sCounter = Counter(s)
    tCounter = Counter(t)

    sCounterKeys = sorted(sCounter.keys())
    tCounterKeys = sorted(tCounter.keys())

    if sCounterKeys == tCounterKeys:
        for i in range(len(sCounterKeys)):
            if not (sCounter[sCounterKeys[i]] == tCounter[tCounterKeys[i]]):
                print(f"{sCounterKeys[i]} : {sCounter[sCounterKeys[i]]}")
                print(f"{tCounterKeys[i]} : {tCounter[tCounterKeys[i]]}")
                return False
        return True
    else:
        return False


isAnagram("nagaram", "anagramm")
