/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    let count = 0;
    let spaceEncountered = true; // start at a non-space character
    s = s.trim();
    for(let i = 0; i < s.length; i++) {
        if(s[i] == " ") {
            spaceEncountered = true;
        }
        if(s[i] != " " && spaceEncountered) {
            spaceEncountered = false;
            count++;
        }
    }

    return count;
};