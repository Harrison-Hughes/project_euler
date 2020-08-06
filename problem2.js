// sum of even numbers in fibonacci sequence with value < 4,000,000 (n)

const problem2 = n => {
  let numToSum = [1, 2];
  while (Math.max(...numToSum) < n) {
    nextNumber = numToSum.slice(-2).reduce(reducer);
    numToSum.push(nextNumber);
  }
};

const reducer = (accumulator, currentValue) => accumulator + currentValue;

const isEven = x => {
  return x % 2 === 0 ? true : false;
};
