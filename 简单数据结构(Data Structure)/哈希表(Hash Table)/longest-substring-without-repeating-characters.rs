use std::collections::HashMap;

impl Solution {
    /* pub fn length_of_longest_substring(s: String) -> i32 {
        let (mut ans, mut cnt) = (0, 0);
        let mut map = HashMap::new();
        let s = s.chars().collect::<Vec<_>>();
        let mut l = 0;

        s.iter().enumerate().for_each(|(i, c)| {
            match map.get(c) {
                None => {
                    cnt += 1;
                    ans = ans.max(cnt);
                }
                Some(&i) => {
                    for c in &s[l..=i] {
                        map.remove(c);
                    }
                    cnt -= i - l;
                    l = i + 1;
                }
            }
            map.insert(*c, i);
        });
        ans as i32
    } */
    // 优化
    pub fn length_of_longest_substring(s: String) -> i32 {
        if s.is_empty() {
            return 0;
        }
        let mut ret = 0;
        let mut l = 0;
        let mut cache = vec![0; 128];

        s.chars().enumerate().for_each(|(i, ch)| {
            l = l.max(cache[ch as usize]);
            ret = ret.max(i as i32 - l + 1);
            cache[ch as usize] = i as i32 + 1;
        });
        ret
    }
}
