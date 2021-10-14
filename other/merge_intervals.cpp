// leetcode 56. mergeIntervals cpp

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) 
    {
        int n = intervals.size();
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ret;
        int cur = 0;
        while(cur < n)
        {
            int max_val = intervals[cur][1];

            if(cur == n - 1)
            {
                ret.push_back(intervals[cur]);
                break;
            }
            for(int seek = cur + 1; seek < n; seek++)
            {
                if(max_val >= intervals[seek][0])
                {
                    if(seek == n - 1)
                    {
                        max_val = max(max_val, intervals[seek][1]);
                        ret.push_back({intervals[cur][0], max_val});
                        cur = n;
                    }
                    max_val = max(max_val, intervals[seek][1]);
                    continue;
                }
                else
                {
                    ret.push_back({intervals[cur][0], max_val});
                    cur = seek;
                    break;
                }
            }
        }
        return ret;
    }
};
