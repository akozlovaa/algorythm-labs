class BubbleSort:
    comparison_counter = 0
    swap_counter = 0

    def bubble_sort_descending(given_list):
        size = len(given_list)
        for i in range(size - 1):
            for j in range(size - i - 1):
                if given_list[j].avg_rate < given_list[j + 1].avg_rate:
                    BubbleSort.comparison_counter += 1
                    given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
                    BubbleSort.swap_counter += 1
