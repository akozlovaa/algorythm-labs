class BubbleSort:
    comparison_counter = 0
    swap_counter = 0

    def bubble_sort_descending(input_array):
        size = len(input_array)
        for i in range(size - 1):
            for j in range(size - i - 1):
                BubbleSort.comparison_counter += 1
                if input_array[j].avg_rate < input_array[j + 1].avg_rate:
                    input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
                    BubbleSort.swap_counter += 1
