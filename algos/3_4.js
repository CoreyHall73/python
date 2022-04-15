//* 
//     String: Is Palindrome
//     Create a function that returns a boolean whether the string is a strict palindrome. 
//     - palindrome = string that is same forwards and backwards
    
//     Do not ignore spaces, punctuation and capitalization
//  */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

// /**
//   * Determines if the given str is a palindrome (same forwards and backwards).
//   * - Time: O(?).
//   * - Space: O(?).
//   * @param {string} str
//   * @returns {boolean} Whether the given str is a palindrome or not.
//   */

    // make str array
    // look at input str
    // reverse input arrat
    // turn back to str
    // compare reverse to original

    // if same
        //return true
    // else
        // return false


function isPalindrome(str) {
    var arrStr = str.split("");
    var revArr = arrStr.reverse();
    var newArr = revArr.join("");
    if (str === newArr) {
        return true;
    } else {
        return false;
    }
}



console.log(isPalindrome(str1))
console.log(isPalindrome(str2))
console.log(isPalindrome(str3))
console.log(isPalindrome(str4))







// DONT CHANGE ANYTHING BELOW THIS LINE !!!!


module.exports = { isPalindrome };




/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided,
    but also at the substrings within it.
    Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/

// const { isPalindrome  }= require("../isPalindrome");


// const str1 = "what up, daddy-o?";
// const expected1 = "dad";

// const str2 = "uh, not much";
// const expected2 = "u";

// const str3 = "Yikes! my favorite racecar erupted!";
// const expected3 = "e racecar e";

// const str4 = "a1001x20002y5677765z";
// const expected4 = "5677765";

// const str5 = "a1001x20002y567765z";
// const expected5 = "567765";

// /**
//  * Finds the longest palindromic substring in the given string.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {string} The longest palindromic substring from the given string.
//  */

// // make var for longest
// // split str into array of words
// // iterate over words
// // rerverse each word
// // if word is pal and > longest
//     //return that word

// function longestPalindromicSubstring(str) {
//     // var longest = arrStr[0];
//     var arrStr = str.split(" ");
//     for (let i = 0; i < arrStr.length; i++) {
//         if (arrStr[i] > longest) {
//             longest = arrStr[i];
//         }
//     }
//     var newStr = arrStr.join("");
//     return longest;
// }




// console.log(longestPalindromicSubstring(str1))
// console.log(longestPalindromicSubstring(str2))
// console.log(longestPalindromicSubstring(str3))
// console.log(longestPalindromicSubstring(str4))
// console.log(longestPalindromicSubstring(str5))