// hot100-lc 338. 比特位计数

class Solution {
public:
    std::vector<int> countBits(int n) {
        std::vector<int> ans = {0};
        for (int i = 1; i <= n; i++)
        {
            if (i % 2 != 0)
            {
                int count = ans[i - 1] + 1;
                ans.push_back(count);
            }
            else
            {
                int count = ans[i / 2];
                ans.push_back(count);
            }
        }
        return ans;
    }
};

