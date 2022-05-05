impl Solution {
    // 贪心
    /* pub fn int_to_roman(num: i32) -> String {
        let mut result = String::new();
        let mut num = num;
        let mut roman = vec![
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I",
        ];
        let mut value = vec![
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1,
        ];
        for i in 0..value.len() {
            while num >= value[i] {
                result.push_str(roman[i]);
                num -= value[i];
            }
        }
        result
    } */
    // 暴力
    pub fn int_to_roman(num: i32) -> String {
        let mut result = String::new();
        let mut M = vec!["", "M", "MM", "MMM"]; // 1000,2000,3000
        let mut C = vec!["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]; // 100~1000
        let mut X = vec!["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]; // 10~90
        let mut I = vec!["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]; // 1~9
        result.push_str(&M[(num / 1000) as usize]);
        result.push_str(&C[((num % 1000) / 100) as usize]);
        result.push_str(&X[((num % 100) / 10) as usize]);
        result.push_str(&I[(num % 10) as usize]);
        result
    }
    /* 
    // https://leetcode-cn.com/problems/integer-to-roman/solution/rustan-shi-jin-zhi-tan-xin-chu-li-by-sea-qp2r/
    这个题解即耗时间又耗空间，不过让我学到rust新的用法，思路是贪心
    pub fn int_to_roman(num: i32) -> String {
        [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")].into_iter()
        .fold((String::with_capacity(20), num), |(mut s, mut num), (base, unit)| {
            (s + &unit.repeat((num / base) as usize), num % base)
        }).0
    }
    */
}
