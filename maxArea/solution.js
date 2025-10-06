var maxArea = function(height) {

    const left = 0
    const right = height.length - 1
    let maxArea = 0
    while(left < right){
         let leftValue = height[left]
         let righValue = height[right]
         if (leftValue < righValue){
            let currentMax = leftValue * (right - left)
            if (maxArea < currentMax)
                maxArea = currentMax;
            left++;
         }
         else{
            let currentMax = righValue * (right - left)
            if(maxArea < currentMax)
                maxArea = currentMax
            right--;
         }

    }
    return maxArea;

    
};
