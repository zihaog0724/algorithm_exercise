void merge(int arr[], int l, int mid, int r)
{

    int left_size = mid - l;
    int right_size = r - mid + 1;
    int *arr_left = new int[left_size];
    int *arr_right = new int[right_size];

    for (int i = l; i < mid; i++)
    {
        arr_left[i-l] = arr[i];
    }


    for (int i = mid; i < r + 1; i++)
    {
        arr_right[i-mid] = arr[i];
    }

    int i = 0, j = 0, k = l;
    while(i < left_size && j < right_size)
    {
        if (arr_left[i] <= arr_right[j])
        {
            arr[k] = arr_left[i];
            i++;
            k++;
        }
        else
        {
            arr[k] = arr_right[j];
            j++;
            k++;
        }
    }

    while(i < left_size)
    {
        arr[k] = arr_left[i];
        i++;
        k++;
    }

    while(j < right_size)
    {
        arr[k] = arr_right[j];
        j++;
        k++;
    }


    delete []arr_left;
    delete []arr_right;
}


void merge_sort(int arr[], int l, int r)
{
    if (l == r)
    {
        return;
    }
    int mid = (l + r) / 2;
    merge_sort(arr, l, mid);
    merge_sort(arr, mid+1, r);
    merge(arr, l, mid+1, r);
}

// test
int main()
{
    int arr[] = {3,2,7,1,5,6,4,8};
    merge_sort(arr, 0, 7);
    for (int i = 0; i < 8; i++)
    {
        std::cout << arr[i] << "; ";
    }
}
