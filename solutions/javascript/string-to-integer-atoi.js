/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    var result = 0;
    result = parseInt(str.trim(), 10);
    if (result <= -Math.pow(2, 31)) {
        return -2147483648;
    } else if (result >= Math.pow(2, 31)) {
        return 2147483647;
    } else if (isNaN(result)) {
        return 0;
    } else {
        return result;
    }
};