import sys
import csv
from time import time
from itertools import combinations

BUDGET = 500


def create_list(file):
    file = open(sys.argv[1])
    reader = csv.reader(file)
    header = next(reader)
    actions = [[r[0], float(r[1]), float(r[1]) * float(r[2]) / 100] for r in reader]
    file.close()

    return header, actions

def bruteforce(dataset):
    best_profit = 0
    best_comb = None
    expense = 0

    for i in range(len(dataset)):
        for comb in combinations(dataset, i + 1):
            price = sum([i[1] for i in comb])
            profit = sum([i[2]for i in comb])
            if price <= BUDGET and profit > best_profit:
                best_profit = profit
                best_comb = comb
                expense = price

    return best_profit, best_comb, expense

def main():
    if len(sys.argv) < 2:
        print("You must specify a file.")
    elif len(sys.argv) != 2:
        print("There are too many arguments specified.")
    else:
        try:
            start_time = time()
            print("\nLoading data...\n")
            header, actions = create_list(sys.argv[1])
        except FileNotFoundError:
            print(f"No such file or directory: '{sys.argv[1]}'\n")

    print("\nBruteforce working, please wait...\n")
    print(f"  {header[0]}        {header[1]}        {header[2]}\n")
    best_profit, best_comb, expense = bruteforce(actions)
    for i in best_comb:
        print(f"{str(i[0])} for {round(float(i[1]), 2)}€ and "
        f"{round(float(i[2]), 2)}€ of profit.")
    print(f"\nTotal profit is : {round(best_profit, 2)}€ for a budget of"
    f" {round(expense, 2)}€.")

    execution_time = round(time() - start_time, 4)
    print(f"\nExecution time: {execution_time}s\n")

if __name__ == "__main__":
    main()
