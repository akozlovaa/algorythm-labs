class HeapSort:
    comparison_counter = 0
    swap_counter = 0

    def heap_sort_ascending(input_array):
        size = len(input_array)
        for i in range(size // 2 - 1, -1, -1):
            HeapSort.heapify(input_array, size, i)
        for i in range(size - 1, 0, -1):
            input_array[i], input_array[0] = input_array[0], input_array[i]
            HeapSort.heapify(input_array, i, 0)

    def heapify(input_array, n, l):
        largest = l
        left = 2 * l + 1
        right = 2 * l + 2

        HeapSort.comparison_counter += 2
        if left < n and input_array[l].num_of_characters < input_array[left].num_of_characters:
            largest = left
            HeapSort.swap_counter += 1

        HeapSort.comparison_counter += 2
        if right < n and input_array[largest].num_of_characters < input_array[right].num_of_characters:
            largest = right
            HeapSort.swap_counter += 1

        HeapSort.comparison_counter += 1
        if largest != l:
            input_array[l], input_array[largest] = input_array[largest], input_array[l]
            HeapSort.swap_counter += 1
            HeapSort.heapify(input_array, n, largest)