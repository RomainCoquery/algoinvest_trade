import sys
import csv
from time import time
from itertools import combinations

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


def bruteforce(dataset):
    best_profit = 0
    best_comb = None

    for i in range(len(dataset)):
        for comb in combinations(dataset, i + 1):
            price = sum([float(i[1]) for i in comb])
            profit = sum([float(i[1]) * float(i[2]) / 100 for i in comb])
            if price <= BUDGET and profit > best_profit:
                best_profit = profit
                best_comb = comb

    total_profit = sum(float(i[1]) for i in best_comb)
    return best_profit, best_comb, total_profit


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

    print("\nBruteforce working, please wait...\n")
    print(f"  {header[0]}        {header[1]}        {header[2]}\n")
    best_profit, best_comb, total_profit = bruteforce(actions)
    for i in best_comb:
        print(f"{str(i[0])} for {round(float(i[1]), 2)}€ and "
        f"{round(float(i[1]) * float(i[2]) / 100, 2)}€ of profit.")
    print(f"\nTotal profit is : {round(best_profit, 2)}€ for a budget of"
    f" {round(total_profit, 2)}€.")

    execution_time = round(time() - start_time, 4)
    print(f"\nExecution time: {execution_time}s\n")


if __name__ == "__main__":
    main()
