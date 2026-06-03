//2,5,8,11,14,17
nums = [14,17,11,5,2]; // 10
// [9,12,13,11,14,15]
for(let i=0;i<nums.length;i++){
    for(let j=i+1;j<nums.length;j++){
        if(nums[i]>nums[j]){
            let temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp;
        }
    }
}

// diff check
// nums = [13,12,9,11,14,15];
let diff=nums[1]-nums[0];
for(let i=0; i<nums.length-1;i++){
    diff = Math.min(nums[i+1]-nums[i], diff)
}
console.log(diff)
for(let i=0;i<nums.length-1;i++){
    if(nums[i+1]-nums[i] != diff){
        console.log(`the missing number is: ${nums[i]+diff}`);
        break;
    }
    console.log(i)
}


let r = [1, 2, 3, 4, 5, 6];
let result = r.map((val) => {
  console.log(val);
  return val - 1;
});

