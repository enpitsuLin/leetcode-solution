/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    num = Math.abs(x);
    var result = 0,
        len = Math.floor(Math.log(num) / Math.log(10)) + 1;

    function tenspower(num) {
        return Math.pow(10, num - 1)
    }
    for (var i = 0; i < len; i++) {
        result += Math.floor((num % 10)) * tenspower(len - i);
        num /= 10;
    }
    if (result > Math.pow(2, 31) - 1 || -result < -Math.pow(2, 31)) {
        return 0;
    } else {
        return x < 0 ? -result : result;
    }
};