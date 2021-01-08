/**
    0ms, faster than 100% of C++ sols
    6.1MB, less than 99.82% of C++ sols
*/

class Solution {
public:
    int mySqrt(int x) {
        long ans = 0;
        long bit = 1l << 16;
        while(bit > 0) {
            ans |= bit;
            if (ans * ans > x) {
                ans ^= bit;
            }
            bit >>= 1;
        }
        return (int)ans;
    }
};
