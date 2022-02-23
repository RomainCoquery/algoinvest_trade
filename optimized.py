import sys
import csv
from time import time

BUDGET = 500
NAME, PRICE, PROFIT_PERCENT, PROFIT_EURO = 0, 1, 2, 3


def create_list(file):
    rows, total_lines, incorrect_lines = [], 0, 0

    file = open(sys.argv[1])
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        total_lines += 1
        if float(row[1]) > 0 and float(row[2]) > 0:
            rows.append(
                [
                    row[NAME], 
                    float(row[PRICE]), 
                    float(row[PROFIT_PERCENT]), 
                    float(row[PRICE]) * float(row[PROFIT_PERCENT]) / 100
                ]
            )
        else:
            incorrect_lines += 1
    file.close()

    return header, rows, total_lines, incorrect_lines

def float_to_int(data):
    return [
        (
            d[NAME], 
            round(d[PRICE] * 100), 
            round(d[PROFIT_PERCENT] * 100), 
            round(d[PROFIT_EURO] * 100)
        ) 
        for d in data
        ]

def int_to_float(data):
    return [
        (
            d[NAME], 
            round((d[PRICE] / 100), 2), 
            round((d[PROFIT_PERCENT] / 100), 2), 
            round((d[PROFIT_EURO] / 100), 2)
        ) 
            for d in data
        ]

def greedy(dataset):
    actions = sorted(dataset, key=lambda x: x[PROFIT_PERCENT])
    actions_selected, expense = [], 0

    while actions:
        action = actions.pop()
        if action[PRICE] + expense < BUDGET:
            actions_selected.append(action)
            expense += action[PRICE]

    return actions_selected

def dynamic(dataset):
    actions = float_to_int(dataset)
    actions_selected = []
    w = BUDGET * 100
    n = len(actions)

    matrix = [[0 for x in range(w + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if actions[i-1][PRICE] <= w:
                matrix[i][w] = max(
                            actions[i-1][PROFIT_EURO] + 
                            matrix[i-1][w-actions[i-1][PRICE]], matrix[i-1][w]
                        )
            else:
                matrix[i][w] = matrix[i-1][w]

    while w >= 0 and n >= 0:
        action = actions[n-1]
        if matrix[n][w] == matrix[n-1][w-action[PRICE]] + action[PROFIT_EURO]:
            actions_selected.append(action)
            w -= action[PRICE]
        n -= 1
    
    return int_to_float(actions_selected)

def choice(data):
    choice = None
    while not choice:
        choice = input("Please choose an algorithm:\n\n"
                        "[1] Greedy (faster)\n"
                        "[2] Dynamic (better)\n\n"
                        ">> "
                        )

        if choice == '1':
            algorithm = greedy(data)
        elif choice == '2':
            algorithm = dynamic(data)

    return algorithm

def main():
    if len(sys.argv) < 2:
        print("You must specify a file.")
    elif len(sys.argv) != 2:
        print("There are too many arguments specified.")
    else:
        try:
            header, rows, total_lines, incorrect_lines = create_list(sys.argv[1])
            start_time = time()
            actions_selected = choice(rows)
        except FileNotFoundError:
            print(f"No such file or directory: '{sys.argv[1]}'\n")

    print(f"\nAnalyzing {total_lines} lines in document\n\n"
            f"Deletion of {incorrect_lines} incorrect lines\n\n"
            f"   {header[0]}       {header[1]}      {header[2]}\n")

    for i in actions_selected:
        print(f"{i[NAME]} for {round(i[PRICE], 2)}€ and "
                f"{round(i[PROFIT_EURO], 2)}€ of profit.")

    print(
    f"\nTotal profit is : {round(sum(i[PROFIT_EURO] for i in actions_selected), 2)}"
    f"€ for a budget of {round(sum(i[PRICE] for i in actions_selected), 2)}€."
    )
    
    execution_time = round(time() - start_time, 4)
    print(f"\nExecution time: {execution_time}s\n")

if __name__ in "__main__":
    main()
