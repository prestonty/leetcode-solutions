/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    let hashmap = new Map();
    let set = new Set();

    list_s = s.split(" ");

    // check if length are same
    if(list_s.length != pattern.length) {
        return false;
    }

    for(let i = 0; i < pattern.length; i++) {
        if(hashmap.has(pattern[i])) {
            if(hashmap.get(pattern[i]) != list_s[i]) {
                return false;
            }
        } else {
            hashmap.set(pattern[i], list_s[i]);
            
            // Ensure that the values in hashmap are unique
            if(set.has(list_s[i])) {
                return false;
            } else {
                set.add(list_s[i]);
            }
        }
    }

    return true;
};