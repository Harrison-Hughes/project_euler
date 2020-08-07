# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def findNthPrime(n)
  primeArray=[2]
  i = 3
  while primeArray.length < n   
    if !nHasFactorInArray(i, primeArray)
      primeArray.push(i)
    end
    i += 1
  end
  p primeArray.last
end

def nHasFactorInArray(n, arr)
  for i in arr do
    if n % i == 0
      return true
    elsif i**2 >= n
      return false
    end
  end
  return false
end