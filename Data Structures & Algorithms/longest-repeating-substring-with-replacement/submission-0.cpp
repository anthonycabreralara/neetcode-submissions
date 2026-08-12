class Solution {
public:
    int characterReplacement(string s, int k) {
        std::unordered_map<char, int> count;
        int res = 0;
        int left = 0;
        for (int right = 0; right < s.size(); right++) {
            count[s[right]] = 1 + count[s[right]];

            int maxFrequency = 0;
            for (const auto& [key, value] : count) {
                maxFrequency = std::max(maxFrequency, value);
            }

            while ((right - left + 1) - maxFrequency > k) {
                count[s[left]] = count[s[left]] - 1;
                left++;
            }

            res = std::max(res, right - left + 1);
        }
        return res;

    }
};
