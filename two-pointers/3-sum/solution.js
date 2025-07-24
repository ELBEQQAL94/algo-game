const threeSum = (nums) => {
  // init output
  let output = [];
  const sorted = nums.sort((a, b) => a - b);

  // iteration through nums
  for (let i = 0; i < sorted.length; i++) {
    // init left, right
    let left = i + 1;
    let right = sorted.length - 1;
    // check for duplicate from i > 0
    if (i > 0 && sorted[i] === sorted[i - 1]) continue;

    // while loop left, right
    while (left < right) {
      // total
      const total = sorted[i] + sorted[left] + sorted[right];

      // check total
      if (total === 0) {
        const group = [sorted[i], sorted[left], sorted[right]];

        output.push(group);

        while (left < right && sorted[right] === sorted[right - 1]) {
          right -= 1;
        }

        while (left < right && sorted[left] === sorted[left + 1]) {
          left += 1;
        }
        left += 1;
        right -= 1;
      } else if (total < 0) {
        left += 1;
      } else {
        right -= 1;
      }
    }
  }
  // return result
  return output;
};
