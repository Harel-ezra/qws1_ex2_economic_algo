
import cvxpy as cp


def egalitarian_division(matrix):
    n=len(matrix) # agents
    m=len(matrix[0]) # resources
    variables = cp.Variable(n * m)

    constraints = []
    min_utility = cp.Variable()

    for a in range (n): # this run on player
        u=0
        for b in range(m):# and this run on resources
            u+=matrix[a][b]*variables[a*m+b]
        constraints.append(min_utility<=u) # find mix min


    for b in range(0, m):  # and this run on resources
        x=0
        for a in range (0,n): # this run on player
            x+=variables[a*m+b]
            constraints.append(variables[a*m+b]>=0) # any agents can get up to 1 from and resource
        constraints.append(x==1) # sum of signal resource is =1

    prob = cp.Problem(
        cp.Maximize(min_utility),
        constraints)

    prob.solve()

    for i in range(n):
        print( "Agent ",i+1, " gets", end =" ")
        for j in range(m):
           print(round(variables[i*m+j].value,2)," of resource ",j+1, end =", ")
        print()


if __name__ == '__main__':
    matrix=[[80,19,1],
            [70,1,29],
            [10,20,70],
            [100,0,0]]
    egalitarian_division(matrix)

