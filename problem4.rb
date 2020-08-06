# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit (n_digit) numbers.

def largestPalindromicNumber(n_digits)
  # palindromes = []
  startPoint = (10**n_digits-1)**2
  endPoint = (10**(n_digits-1))**2
  i = startPoint
  while i >= endPoint do
    if isAPalindrome(i) && isNumAProductOfTwoNDigitNumbers(i, n_digits)
      puts i
      return i
    end
    i -= 1
  end
  p 'no product/palindromes found'
end

def isAPalindrome(n)
  stringNum = n.to_s
  if stringNum == stringNum.reverse
    return true
  else return false
  end
end

def isNumAProductOfTwoNDigitNumbers(num, n)
  i = 10**n-1
  while i >= 10**(n-1)
    if num % i === 0
      if (num / i).to_s.length == n
        return true
        break
      else i -=1
      end
    else i -= 1
    end
  end
  return false
end