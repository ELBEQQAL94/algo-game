const twoSum = (numbers, target) => {
    const new_numbers = [0, ...numbers];
    let left = 1;
    let right = new_numbers.length - 1;

    while (left < right) {
        if (new_numbers[left] + new_numbers[right] === target) {
            return [left, right];
        }

        if (new_numbers[left] + new_numbers[right] > target) {
            right -= 1;
        } 

        if (new_numbers[left] + new_numbers[right] < target) {
            left += 1;
        }
    }
};