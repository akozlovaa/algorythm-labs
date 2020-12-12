import csv
import time

from managers.bubble_sort import BubbleSort
from managers.heap_sort import HeapSort
from model.game import Game

list_of_games = []

with open('../../PycharmProjects/algorythms-lab-1/myFile0.csv', 'r', encoding='utf-8') as file:
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
    print(f'\n\n\n\n\n')

    heap_start_time = time.time()
    HeapSort.heap_sort_ascending(list_of_games)
    heap_end_time = time.time()

    print('Games sorted by number of characters:')
    for game in list_of_games:
        print(str(game))
    print(f'\n\n\n\n\n')

    print("----BUBBLE SORT----")
    print(f'{bubble_end_time - bubble_start_time} seconds for bubble sort ')
    print(f'{BubbleSort.swap_counter} number of swaps ')
    print(f'{BubbleSort.comparison_counter} number of swaps ')

    print("----HEAP SORT----")
    print(f'{heap_end_time - heap_start_time} seconds for heap sort ')
    print(f'{HeapSort.swap_counter} number of swaps ')
    print(f'{HeapSort.comparison_counter} number of swaps ')
