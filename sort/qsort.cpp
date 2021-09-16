#include <iostream>
#include <tuple>

std::tuple<int, int> partition(int arr[], int left, int right)
{
    int less, cur, more, pivot;
    less = left - 1;
    cur = left;
    more = right + 1;
    pivot = arr[right];

    while (cur < more)
    {
        if (arr[cur] < pivot)
        {
            int tmp = arr[cur];
            arr[cur] = arr[less+1];
            arr[less+1] = tmp;
            less++;
            cur++;
        }
        else if (arr[cur] == pivot)
        {
            cur++;
        }
        else
        {
            int tmp = arr[cur];
            arr[cur] = arr[more-1];
            arr[more-1] = tmp;
            more--;
        }
    }
    std::tuple<int, int> boundary = std::make_tuple(less, more);
    return boundary;
}

void qsort(int arr[], int left, int right)
{
    if (left >= right)
    {
        return;
    }
    std::tuple<int, int> boundary;
    boundary = partition(arr, left, right);
    qsort(arr, left, std::get<0>(boundary));
    qsort(arr, std::get<1>(boundary), right);
}

// test
int main()
{
    int arr[] = {3,2,7,1,8,6,4,5};
    qsort(arr, 0, 7);
    for (int i : arr)
    {
        std::cout << i << "; ";
    }
}
