#include <iostream>
#include <vector>
#include <string>

using namespace std;

int NumberOfSetBits(int i)
{
     // Java: use >>> instead of >>
     // C or C++: use uint32_t
     i = i - ((i >> 1) & 0x55555555);
     i = (i & 0x33333333) + ((i >> 2) & 0x33333333);
     return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
}

class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> array;
        for(auto w : words){
            int cur = 0;
            //cout << w << endl;
            for(auto c : w){
                //cout << c << endl;
                cur = cur | 1<<int(c-'a');
            }
            //cout << cur << endl;
            array.push_back(cur);
        }
        int ans = 0;
        //cout << array.size() << endl;
        for(int i = 0; i < array.size(); ++i)
            for(int j = i+1; j < array.size();++j){
                //cout << (array[i] & array[j]) << endl;
                if ((array[i] & array[j]) == 0){
                    //cout << i << " " << j << endl;
                    if (words[i].length() * words[j].length() > ans){
                        ans = words[i].length() * words[j].length();
                    }
                }
            }
        return ans;
    }
};

int main(){
    Solution sol;
    vector<string> words = {"abcw", "baz", "foo", "bar", "xtfn", "abcdef"};
    cout << sol.maxProduct(words) << endl;

    return 0;
}
