#include <iostream>

void bubble(int arr[], int n)
/*
 * n是数组长度
 */
{
    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i] > arr[i+1])
        {
            int tmp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = tmp;
        }
    }
}


void bubble_sort(int arr[], int n)
/*
 * n是数组长度
 */
{
    for (int i = n - 1; i >= 0; i--)
    {
        bubble(arr, i+1);
    }
}

// test
int main()
{
    int arr[] = {3,6,4,1,2,7,5};
    int length = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, length);
    for (int i = 0; i < length; i++)
    {
        std::cout << arr[i] << "; ";
    }
}
