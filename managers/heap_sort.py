class HeapSort:
    comparison_counter = 0
    swap_counter = 0

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i].num_of_characters < arr[l].num_of_characters:
            HeapSort.comparison_counter += 2
            largest = l
            HeapSort.swap_counter += 1

        if r < n and arr[largest].num_of_characters < arr[r].num_of_characters:
            HeapSort.comparison_counter += 2
            largest = r
            HeapSort.swap_counter += 1

        if largest != i:
            HeapSort.comparison_counter += 1
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.swap_counter += 2
            HeapSort.heapify(arr, n, largest)

    def heap_sort_ascending(arr):
        n = len(arr)
        for i in range(n // 2, -1, -1):
            HeapSort.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            HeapSort.heapify(arr, i, 0)
