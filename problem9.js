// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

// a2 + b2 = c2
// For example, 32 + 42 = 9 + 16 = 25 = 52.

// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

const sumTo1000 = (a, b, c) => {
  if (a + b + c === 1000) return true;
  else return false;
};

const pythagoreanTriplet = (a, b, c) => {
  if (a ** 2 + b ** 2 === c ** 2) return true;
  else return false;
};

const calculatePythagoreanTripletWhichSumsToN = (n) => {
  let [a, b, c] = [1, 2, n - 3];
  let solution = false;

  while (!solution) {
    if (pythagoreanTriplet(a, b, c)) solution = [a, b, c];
    else if (!sumTo1000(a, b, c) || a > b || a > c || b > c)
      solution = "error in func";
    else {
      if (b + 1 < c - 1) {
        [b, c] = [b + 1, c - 1];
      } else {
        [a, b, c] = [a + 1, a + 2, n - 2 * a - 3];
      }
    }
  }

  if (!!solution) return solution;
  else return "no solution";
};

const calculateProductOFTriplet = (arr) => {
  return arr[0] * arr[1] * arr[2];
};

console.log(
  calculateProductOFTriplet(calculatePythagoreanTripletWhichSumsToN(1000))
);
