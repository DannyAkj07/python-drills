def number(values, target):
    for i, num in enumerate(values):
        if num == target:
            response = f"Found at index {i}"
            break
    else:
        response = "Target not found"

    return response


values = [14, 7, 22, 9, 7, 22, 31]
print(number(values, 7))

# ==========OR========

# def number(values, target):
#     for i, num in enumerate(values):
#         if num == target:
#             return f"Found at index {i}"
#     else:
#         return "Target not found"


# values = [14, 7, 22, 9, 7, 31]
# print(number(values, 7))

def number(values, target):
    for i, num in enumerate(values):
        if num == target:
            response = f"Found at index {i}"
            break
        else:
            response = "Target not found"

    return response


values = [14, 7, 22, 9, 7, 22, 31]
print(number(values, 22))
