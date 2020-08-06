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

let [a, b, c] = [1, 2, 997];
