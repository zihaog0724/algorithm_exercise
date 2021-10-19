// leetcode 84. largestRectangleArea cpp

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) 
    {
        heights.insert(heights.begin(), 0);
        heights.insert(heights.end(), 0);
        stack<int> stk;
        int ret = 0;
        for(int i = 0; i < heights.size(); i++)
        {
            while(!stk.empty() && heights[stk.top()] > heights[i])
            {
                int h = heights[stk.top()];
                stk.pop();
                ret = max(ret, h * (i - stk.top() - 1));
            }
            stk.push(i);
        }
        return ret;
    }
};
