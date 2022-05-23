/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    var result = [];
    result = s.replace(/^\s+|\s+$/g, "").split("").join("")
    if (result === "0") { return true; }
    var patt = /\d+|^[+-]?\d+|\d+[e|.]?\d+|\d+e?\d+\.?\d*|\d+.?\d+e\d*|^\.\d+/g
    if (result.search(patt) === -1) {
        console.log("NaN");
        return false;
    }
    if (result.search(/^e|e$|^\.e|e\.$|^\.\d+\.$|\.{2,}|[A-d]|[f-z]|\s|\d+e+[+-]e+\d+|\.\d+\+|[+-]$|^\.[+-]|[+-]\.$|e\d*\.|\d+e\d+\.\d+|-e|\d+[+-]{1,}\d+/g) !== -1) {
        console.log("searched");
        return false;
    }
    if (result.split(/\./g).length > 2 || result.split(/e/g).length > 2) {
        console.log("long");
        return false;
    }
    return true;
};

console.log(isNumber("2e0e212"));
/**
 * 吐槽：
 *  给的样例和问题描述实在是太模糊了，基本是一步步测出来的正则方法，应该会有更好的思路
 */