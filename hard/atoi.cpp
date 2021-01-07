/**
    4ms, faster than 70.03% of C++ solutions
    7.4MB, less than 13.59% of C++ solutions
*/
    
class Solution {
public:
    int myAtoi(string s) {
        long long int result = 0;
        int indicator = 1;
        int i;
        try{
            i = s.find_first_not_of(' ');
        }
        catch(...){
            return 0;
        }
        if(i >= s.length()){
            return 0;
        }
        
        if(s[i] == '-' || s[i] == '+')
            indicator = (s[i++] == '-')? -1 : 1;
        
        while('0'<= s[i] && s[i] <= '9') 
        {
            result = result*10 + (s[i++]-'0');
            if(result*indicator >= INT_MAX) return INT_MAX;
            if(result*indicator <= INT_MIN) return INT_MIN;                
        }
        
        return result*indicator;
    }

};
