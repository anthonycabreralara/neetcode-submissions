#include <string>
#include <unordered_map>
#include <vector>
#include <climits>

class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty()) {
            return "";
        }

        std::unordered_map<char, int> countT;
        for (char c : t) {
            countT[c]++;
        }

        std::unordered_map<char, int> window;
        int have = 0;
        int need = countT.size();
        std::vector<int> res = {0, 0};
        int resLen = INT_MAX;
        int l = 0;

        for (int r = 0; r < s.size(); r++) {
            char c = s[r];
            window[c]++;

            if (countT.find(c) != countT.end() && window[c] == countT[c]) {
                have++;
            }

            while (have == need) {
                if (r - l + 1 < resLen) {
                    res = {l, r};
                    resLen = r - l + 1;
                }

                window[s[l]]--;
                if (countT.find(s[l]) != countT.end() && window[s[l]] < countT[s[l]]) {
                    have--;
                }
                l++;
            }
        }

        return resLen == INT_MAX ? "" : s.substr(res[0], resLen);
    }
};