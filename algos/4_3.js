
/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    let pBalance = 0;
    let cBalance = 0;
    let sBalance = 0;
    let tempStr = "";
    let clArr = [')', '}', ']'];
    for (let i = 0; i < str.length; i++) {
        if (str[i] === ')') {
            let openB = '('
            let openInd = 0;
            for (let j = 0; j < tempStr.length; j++) {
                if (tempStr[j] === openB) {
                    openInd === j;
                    break;
                }
            }
            let ts2 =  tempStr.slice(openInd);
            for (let j = 0; j <ts2.length; j++) {
                switch(ts2[j]) {
                    case '(':
                        pBalance++
                        break;
                    case '{':
                        cBalance++
                        break;
                    case '[':
                        sBalance++
                        break;
                    case ')':
                        pBalance--
                        break;
                    case '}':
                        cBalance--
                        break;
                    case ']':
                        sBalance--
                        break;
                }
            }
            if (pBalance !== 0 || cBalance !== 0 || sBalance !== 0) {
                return false;
            }
            else {
                tempStr = tempStr.slice(0, openInd);
                pBalance = sBalance  = cBalance = 0;
            }
        } 
        if (str[i] === '}') {
            let openB = '{'
            let openInd = 0;
            for (let j = 0; j < tempStr.length; j++) {
                if (tempStr[j] === openB) {
                    openInd === j;
                    break;
                }
            }
            let ts2 =  tempStr.slice(openInd);
            for (let j = 0; j <ts2.length; j++) {
                switch(ts2[j]) {
                    case '(':
                        pBalance++
                        break;
                    case '{':
                        cBalance++
                        break;
                    case '[':
                        sBalance++
                        break;
                    case ')':
                        pBalance--
                        break;
                    case '}':
                        cBalance--
                        break;
                    case ']':
                        sBalance--
                        break;
                }
            }
            if (pBalance !== 0 || cBalance !== 0 || sBalance !== 0) {
                return false;
            }
            else {
                tempStr = tempStr.slice(0, openInd);
                pBalance = sBalance  = cBalance = 0;
            }
        } 
        if (str[i] === ']') {
            let openB = '['
            let openInd = 0;
            for (let j = 0; j < tempStr.length; j++) {
                if (tempStr[j] === openB) {
                    openInd === j;
                    break;
                }
            }
            let ts2 =  tempStr.slice(openInd);
            for (let j = 0; j <ts2.length; j++) {
                switch(ts2[j]) {
                    case '(':
                        pBalance++
                        break;
                    case '{':
                        cBalance++
                        break;
                    case '[':
                        sBalance++
                        break;
                    case ')':
                        pBalance--
                        break;
                    case '}':
                        cBalance--
                        break;
                    case ']':
                        sBalance--
                        break;
                }
            }
            if (pBalance !== 0 || cBalance !== 0 || sBalance !== 0) {
                return false;
            }
            else {
                tempStr = tempStr.slice(0, openInd);
                pBalance = sBalance  = cBalance = 0;
            }
        } 
    }
    return (tempStr.length > 0 ? false:true);
}

console.log(bracesValid(str1))
console.log(bracesValid(str2))
console.log(bracesValid(str3))



// /* 
// Parens Valid
// Given an str that has parenthesis in it
// return whether the parenthesis are valid
// */

// const str1 = "Y(3(p)p(3)r)s";
// const expected1 = true;

// const str2 = "N(0(p)3";
// const expected2 = false;
// // Explanation: not every parenthesis is closed.

// const str3 = "N(0)t ) 0(k";
// const expected3 = false;
// // Explanation: because the second ")" is premature: there is nothing open for it to close.

// const strCorey = "((()))((()))";
// const str4 = "a(b))(c";
// const expected4 = false;
// // Explanation: same number of opens and closes but the 2nd closing closes nothing.

// /**
//  * Determines whether the parenthesis in the given string are valid.
//  * Each opening parenthesis must have exactly one closing parenthesis.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {boolean} Whether the parenthesis are valid.
//  */
// function parensValid(str) {
//     let close = 0;
//     let open = 0;
//     for (var i = 0; i < str.length; i++) {
//         if (str[i] === ")" && close === open) {
//             return false;
//         } 
//         else if (str[i] === ")") {
//             close++;
//         }
//         else if (str[i] === "(") {
//             open++;
//         }
//     }
//     return (close === open ? true : false)
//     // if (close === open) {
//     //     return true;
//     // } else {
//     //     return false;
//     // }
// }

// console.log(parensValid(str1))
// console.log(parensValid(str2))
// console.log(parensValid(str3))
// console.log(parensValid(str4))
// console.log(parensValid(strCorey))