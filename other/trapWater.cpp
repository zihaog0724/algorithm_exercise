/*
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
*/

#include <iostream>
#include <vector>
#include <algorithm>

int trap(std::vector<int> & arr)
{
    int left, right, max_left, max_right, res;
    left = 0;
    right = arr.size() - 1;
    max_left = arr[left];
    max_right = arr[right];
    res = 0;

    while (left < right)
    {
        max_left = std::max(arr[left], max_left);
        max_right = std::max(arr[right], max_right);
        if (max_left < max_right)
        {
            res += (max_left - arr[left]);
            left++;
        }
        else
        {
            res += (max_right - arr[right]);
            right--;
        }
    }
    return res;
}

int main()
{
    std::vector<int> arr{0,1,0,2,1,0,1,3,2,1,2,1};
    int res;
    res = trap(arr);
    std::cout << res << std::endl;
}
