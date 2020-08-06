# sum of even numbers in fibonacci sequence with value < 4,000,000 (n)

def problem2(n)
  fibonacciNumbers = [1, 2]
  while fibonacciNumbers.max < n
    nextNum = fibonacciNumbers[-1] + fibonacciNumbers[-2]
    fibonacciNumbers.push(nextNum)
  end
  fibonacciNumbers.pop
  return sumIfEven(fibonacciNumbers)
end

def sumIfEven(arr)
  arr.select{ |n| n.even? }.sum
end