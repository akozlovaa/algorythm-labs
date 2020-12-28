import csv
import time

from managers.bubble_sort import BubbleSort
from managers.heap_sort import HeapSort
from model.game import Game

list_of_games = []

with open('listOfGames.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for line in csv_reader:
        list_of_games.append(Game(name=(line[0]), num_of_characters=int(line[1]),
                                  avg_rate=float(line[2])))
if __name__ == '__main__':

    bubble_start_time = time.time()
    BubbleSort.bubble_sort_descending(list_of_games)
    bubble_end_time = time.time()
    print('Games sorted by rate:')
    for game in list_of_games:
        print(str(game))

    print(f'\n')

    heap_start_time = time.time()
    HeapSort.heap_sort_ascending(list_of_games)
    heap_end_time = time.time()
    print('Games sorted by num_of_characters:')
    for game in list_of_games:
        print(str(game))

    print(f'\n')

    print("Bubble sort:")
    print(f'{bubble_end_time - bubble_start_time} bubble sort duration (in seconds)')
    print(f'{BubbleSort.comparison_counter} number of comparisons')
    print(f'{BubbleSort.swap_counter} number of swaps')


    print(f'\n')

    print("Heap sort:")
    print(f'{heap_end_time - heap_start_time} heap sort duration (in seconds)')
    print(f'{HeapSort.comparison_counter} number of comparisons')
    print(f'{HeapSort.swap_counter} number of swaps')

