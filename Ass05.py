# N Queen 
def queen(n):
    def backTrack(i):
        if i == n:
            result.append(list(board))
        for j in range(n):
            if j not in column and j-i not in diagonal and j+i not in ofDiagonal:
                column.add(j)
                diagonal.add(j-i)
                ofDiagonal.add(j+i)
                board.append("-" * j + "Q" + "-" * (n-j-1))
                backTrack(i+1)
                column.remove(j)
                diagonal.remove(j-i)
                ofDiagonal.remove(j+i)
                board.pop()

    result = []
    board = []
    column = set()
    diagonal = set()
    ofDiagonal = set()

    backTrack(0)
    return result


pp = int(input("Enter a number"))
p = queen(pp)
for j in p[0]:
    for i in j:
        print(i,end=" ")
    print()