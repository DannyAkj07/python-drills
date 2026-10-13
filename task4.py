def words(text):
    count = 0
    for char in text:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count < 0:
            return "Not balanced"
        
    # if count == 0:
    #     return "Balanced"
    # else:
    #     return "Not balanced"
    return "Balanced" if count == 0 else "Not balanced"


text = "(a+b)"
print(words(text))
