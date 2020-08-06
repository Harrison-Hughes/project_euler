
def largestPrimeFactor(n)
primeFactors = [1]
number = n
f = 2
  while f <= n/(primeFactors.max)
    if number%f==0
      primeFactors.push(f)
      number = number / f
    else f+=1
    end
  end 
return primeFactors.max
end