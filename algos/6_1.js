// /* 
// Recursive Sigma
// Input: integer
// Output: sum of integers from 1 to Input integer
// */

// const num1 = 5;
// const expected1 = 15;
// // Explanation: (1+2+3+4+5)

// const num2 = 2.5;
// const expected2 = 3;
// // Explanation: (1+2)

// const num3 = -1;
// const expected3 = 0;
// const Corey = 41;

// /**
//  * Recursively sum the given int and every previous positive int.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {number} num
//  * @returns {number}
//  */
// function recursiveSigma(num) {
//     let number = parseInt(num);
//     if (isNaN(number)) {
//         return null;
//     }
//     if (number <= 0) {
//         return 0;
//     }
//     return number + recursiveSigma(number - 1);
// } 

// // console.log(recursiveSigma(num1));
// // console.log(recursiveSigma(num2));
// // console.log(recursiveSigma(num3));
// console.log(recursiveSigma(Corey));


/* 
Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;
const Corey = [4,4,4,4];

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums=[], i = 0) {
    if (i === nums.length) {
        return 0;
    }
    return nums[i] + sumArr(nums, i + 1);
}

console.log(sumArr(nums1))
console.log(sumArr(nums2))
console.log(sumArr(nums3))
console.log(sumArr(Corey))