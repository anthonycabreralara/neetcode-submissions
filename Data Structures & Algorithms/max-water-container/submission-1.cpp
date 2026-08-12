class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int max_water = 0;
        while (left < right) {
            int result = (right - left) * std::min(heights[left], heights[right]);
            max_water = std::max(max_water, result); 
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            } 
        }

        return max_water;
    }
};
