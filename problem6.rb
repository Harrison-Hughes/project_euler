# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+102=385

# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2=55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumSquareDiffUpToN(n)
  return squaresOfSum(n) - sumOfSquares(n)
end

def sumOfSquares(n)
  total = 0
  for i in 1..n do
    total += i**2
  end 
  return total
end

def squaresOfSum(n)
  total = 0
  for i in 1..n do
    total += i
  end 
  return total**2
end