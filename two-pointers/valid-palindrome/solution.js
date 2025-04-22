const isPalindrome = (s) => {
    const regex = /[a-zA-Z0-9]/g;
    const new_string = s.match(regex);

    if (new_string.length === 1) return false;

    let left = 0;
    let right = new_string ? new_string.length - 1  : 0;

    while(left < right) {
        if (new_string[left].toLowerCase() != new_string[right].toLowerCase()) {
            return false;
        }

        left += 1;
        right -= 1;
    }

    return true;
}

// const input = "A man, a plan, a canal: Pana,_ma@";
const input = "0P";

console.log(isPalindrome(input));