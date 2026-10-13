
def rows(matrix):
    if not matrix:
        return 'Matrix is empty'
    
    result = []
    for box in matrix:
        row_total = 0
        for row in box:
            row_total += row
        result.append(row_total)
    return f"Row 1 total: {result[0]}\nRow 2 total: {result[1]}\nRow 3 total: {result[2]}"
    

matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
print(rows(matrix))
