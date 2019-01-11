'''Solving systems of equations with matrices
Peter Farrell
January 10, 2019'''

def gauss(A):
    '''Solving a n x n+1 augmented matrix'''
    for j,w in enumerate(A):
        #diagonal term to be 1
        #by dividing row by diagonal term
        if w[j] != 0:
            divisor = w[j]
            for i,v in enumerate(w):
                w[i] = v / divisor
            
        #add the other rows to additive inverse to make value 0
        rowList = [x for x in range(len(A))]
        rowList.remove(j)
        for i in rowList:
            addinv = -1*A[i][j]
            for ind,value in enumerate(A[i]):
                A[i][ind] = value + addinv*A[j][ind]

    return A

B = [[-1,1,-1,-14],[2,-1,1,21],[3,2,1,19]]
C = [[2,0,3,3],[4,-3,7,5],[8,-9,15,9]]
D = [[4,-2,1,2],[1,1,1,-1],[4,2,1,-6]]
E = [[0.03,0.04,0.06,74000],[1,1,1,1500000],[-4,0,1,0]]

#Center of Math System:
F = [[1,-2,-1,0,0], #a = 2*b + c
     [0,-1,2,1,0],  #b = 2*c + d
     [1,0,-2,1,1],  # 2*c = d + a - 1
     [1,0,-1,-1,0]] # d = a - c

print(gauss(F))
'''
output:
[[1.0, 0.0, 0.0, 0.0, 0.33333333333333326],
[0.0, 1.0, 0.0, 0.0, 0.2222222222222222],
[0.0, 0.0, 1.0, 0.0, -0.1111111111111111],
[-0.0, -0.0, -0.0, 1.0, 0.4444444444444444]]
'''
