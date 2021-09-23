// leetcode 69. mySqrt

class Solution {
public:
    int mySqrt(int x)
    {
        if(x == 0 or x == 1)
        {
            return x;
        }

        int low = 0;
        int high = x;
        while(low <= high)
        {
            int mid = (low + high) / 2;
            if ((mid <= x / mid) && ((mid+1) > x / (mid + 1)))
            {
                return mid;
            }
            if (mid > x / mid)
            {
                high = mid;
            }
            if (mid < x / mid)
            {
                low = mid;
            }
        }
    }
};
