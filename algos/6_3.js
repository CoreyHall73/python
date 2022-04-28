/*
    Recursive Binary Search
    Input: SORTED array of ints, int value
    Output: bool representing if value is found
    Recursively search to find if the value exists, do not loop over every element.
    Approach:
    Take the middle item and compare it to the given value.
    Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

const Corey = [2,4,6,8,10,12];
const searchCorey = 7;



/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
function binarySearch(sortedNums, searchNum) {
    let i = sortedNums.length / 2;
    i = parseInt(i);
    // console.log(i);
    if (searchNum === sortedNums[i]) {
        return true;
    } if (i === 0) {
        return false;
    } if (searchNum > sortedNums[i]) {
        return binarySearch(sortedNums.slice(i, sortedNums.length), searchNum)
    } else {
        return binarySearch(sortedNums.slice(0, i), searchNum)
    } 
}

console.log(binarySearch(nums1, searchNum1));
console.log(binarySearch(nums2, searchNum2));
console.log(binarySearch(nums3, searchNum3));
console.log(binarySearch(Corey, searchCorey));



/* 
    Recursively reverse a string
    helpful methods:
    str.slice(beginIndex[, endIndex])
    returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";

const Corey = "House Dogs"

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
function reverseStri(str) {
    let i = str.length - 1;
    if (str === "") {
        return "";
    } 
    return str.charAt(i) + reverseStri(str.slice(0,i));
}

console.log(reverseStri(str1));
console.log(reverseStri(str2));
console.log(reverseStri(Corey));




