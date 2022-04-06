# Python Driver Code

def solve(n: int) -> str:
  # Your code goes here
  # n is the given input
  if n//2==0 or n//7==0:
    return "Special"
 else:
    return "Regular"

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
