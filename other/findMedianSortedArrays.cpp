// leetcode 4. findMedianSortedArrays cpp

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) 
    {
        int l = 0;
        int r = 0;
        int n1 = nums1.size();
        int n2 = nums2.size();
        vector<int> arr;
        while(l < n1 && r < n2)
        {
            if(nums1[l] <= nums2[r])
            {
                arr.push_back(nums1[l]);
                l++;
            }
            else
            {
                arr.push_back(nums2[r]);
                r++;
            }
        }

        while(l < n1)
        {
            arr.push_back(nums1[l]);
            l++;   
        }

        while(r < n2)
        {
            arr.push_back(nums2[r]);
            r++;   
        }

        int n = arr.size();
        if(n % 2 != 0)
        {
            return (double)(arr[n/2]);
        }
        else
        {
            return 0.5 * (double)(arr[n/2] + arr[n/2-1]);
        }
    }
};
