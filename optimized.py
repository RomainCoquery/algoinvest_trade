import sys
import csv
from time import time

BUDGET = 500


def create_list(file):
    file = open(sys.argv[1])
    csvreader = csv.reader(file)
    header = next(csvreader)
    actions = []
    incorrect_lines = 0
    for action in csvreader:
        if float(action[1]) > 0.0 and float(action[2]) > 0.0:
            actions.append(action)
        else:
            incorrect_lines += 1
    file.close()
    return header, actions, incorrect_lines

def greedy(dataset):
    actions = dataset
    actions_sort = sorted(actions, key=lambda x: float(x[2]) / 100)
    actions_selected = []
    expense = 0

    while actions_sort:
        action = actions_sort.pop()
        if float(action[1]) + expense < BUDGET:
            actions_selected.append(action)
            expense += float(action[1])

    total_profit = sum(float(i[1]) * float(i[2]) / 100 for i in actions_selected)
    return actions_selected, expense, total_profit


def main():
    start_time = time()

    if len(sys.argv) < 2:
        print("You must specify a file.")
    elif len(sys.argv) != 2:
        print("There are too many arguments specified.")
    else:
        try:
            print("\nLoading data...\n")
            header, actions, incorrect_lines = create_list(sys.argv[1])
            print(f"Deletion of {incorrect_lines} incorrect lines")
        except FileNotFoundError:
            print(f"No such file or directory: '{sys.argv[1]}'\n")

    print("\nOptimized working, please wait...\n")
    print(f"  {header[0]}        {header[1]}        {header[2]}\n")
    
    actions_selected, expense, total_profit, = greedy(actions)
    for i in actions_selected:
        print(f"{i[0]} for {round(float(i[1]), 2)}€ and "
        f"{round(float(i[1]) * float(i[2]) / 100, 2)}€ of profit.")
    print(f"\nTotal profit is : {round(total_profit, 2)}€ for a budget of"
    f" {round(expense, 2)}€.")

    execution_time = round(time() - start_time, 4)
    print(f"\nExecution time: {execution_time}s\n")


if __name__ == "__main__":
    main()
