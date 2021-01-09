/**
    24ms, faster than 40.43% of C++ sol
    8.1MB, less than 51.55% of C++ sol
*/

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> T = { { 'I' , 1 },
                                   { 'V' , 5 },
                                   { 'X' , 10 },
                                   { 'L' , 50 },
                                   { 'C' , 100 },
                                   { 'D' , 500 },
                                   { 'M' , 1000 } };
                                   
    int sum = T[s.back()];
    for (int i = s.length() - 2; i >= 0; --i) 
    {
        if (T[s[i]] < T[s[i + 1]])
        {
            sum -= T[s[i]];
        }
        else
        {
            sum += T[s[i]];
        }
    }
   
    return sum;
    }
};
