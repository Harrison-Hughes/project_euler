# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 (n to m)?

def smallestNumEvenlyDivisibleFromNToM(n, m)
  numbers = [];
  for i in n..m do 
    numbers.push(i)
  end
  numbers = filterFactorsFromArray(numbers)
  p numbers
  i = 1
  while i > 0
    if evenlyDivisibleByArray(i, numbers) 
      p i
      return i
    else i += 1
    end
  end
end

def filterFactorsFromArray(arr)
  return arr.select{ |n| n>=(arr.max.to_f/2).ceil}
end

def evenlyDivisibleByArray(n, arr)
  for i in arr do
    if n % i != 0
      return false
    end
  end
  return true
end