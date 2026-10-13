
def rows(matrix):
    if not matrix:
        return 'Matrix is empty'
    
    result = []
    for i,box in enumerate(matrix,start=1):
        row_total = 0
        for row in box:
            row_total += row
        result.append(f"Row {i} total: {row_total}")
        
    return "\n".join(result)
    

matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
print(rows(matrix))
