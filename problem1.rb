def multiplesOfThreeAndFive(n)
  total = 0
  for i in 1..n-1 do
   if i%3==0 || i%5==0
    total += i
   end
  end
  return total
end