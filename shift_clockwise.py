def output_matrix(M):
    for i in M:
        for j in i:
            print('{: >2}'.format(j), end = ' ')
        print()
    print()
k=0
n=int(input('Size: '))
matrix = [[ k:=k+1 for j in range(n)] for i in range(n)]
#n = 5
#matrix = [ [1, 2, 3, 4, 5], \
#           [6, 7, 8, 9, 10], \
#           [11, 12, 13, 14, 15], \
#           [16, 17, 18, 19, 20], \
#           [21, 22, 23, 24, 25] ]
output_matrix(matrix)

for i in range( (n+1)//2 ):

    if (i+1)%2:

        # clockwise

        #up
        prev = matrix[i][i]
        for j in range(i+1, n-i):
            curr  = matrix[i][j]
            matrix[i][j] = prev
            prev = curr

        # right
        prev = curr
        for j in range(i+1, n-i):
            curr = matrix[j][n-i -1]
            #print(curr, j)
            matrix[j][n-i -1] = prev
            prev = curr

        # down
        prev = curr
        for j in range(n-i -1 -1, i-1, -1):
            curr = matrix[n-i -1][j]
            matrix[n-i -1][j] = prev
            prev = curr
            
        # left
        prev = curr
        for j in range(n-i-1 -1, i-1, -1):
            curr = matrix[j][i]
            matrix[j][i] = prev
            prev = curr

    
    
    else:
        # counterclockwise
        

        #left
        prev = matrix[i][i]
        for j in range(i+1, n-i):
        
            curr  = matrix[j][i]
            #print(j, i, curr, prev)
            matrix[j][i] = prev
            #print('trr')
            #output_matrix(matrix)
            prev = curr
            #print(prev)
            #print()
        #print()

        

        # down
        prev = curr
        #print(prev)
        for j in range(i+1, n-i):
            curr = matrix[n -i - 1][j]
            matrix[n-i -1][j] = prev
            prev = curr

        

        # right
        prev = curr
        #print(prev)
        for j in range(n-i -1 -1, i-1, -1):
            curr = matrix[j][n-i -1]
            
            matrix[j][n-i -1] = prev
            prev = curr
        
        
        
        # up
        prev = curr
        for j in range(n-i-1 -1, i-1, -1):
            curr = matrix[i][j]
            matrix[i][j] = prev
            prev = curr
        

    
            
output_matrix(matrix)
