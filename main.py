#This program shows all the possible ways to reach 100 points in a basketball game where we can score 1 point(freethrow), 2 points(layup), or 3 points(three-pointer)

def waysToScore(n):
    
    maxPoints = 3
    
    while(n < 1):
        n = int(input("You must score atleast 1 point! Please try again:"))
    
    ways = [ [ (0,) ] ] + [0] * n
    
    for j in range(1, n+1):
        ways[j] = [w + (j,) for ws in ways[max(0, j-maxPoints):j] for w in ws]
    return ways[n]



desiredPoints = int(input("Enter a point value you would like to see all combinations for: "))
print(waysToScore(desiredPoints))
