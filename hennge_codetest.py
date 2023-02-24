def main():
    # number of test case input
    test_cases = int(input())
    results = []

    process_input(test_cases, results)

    # prints the list of results with each result separated by a newline
    print(*results, sep="\n")


def process_input(test_cases, results):
    if test_cases == 0:
        return
    _ = int(input())

    numbers = list(map(int, input().split()))

    # calculate sum of squares
    sum_of_squares(numbers, results)

    test_cases -= 1
    process_input(test_cases, results)


def sum_of_squares(numbers, results):
    # filter negative numbers since they don't contribute to sum
    numbers_excluding_negatives = list(filter(lambda number: number >= 0, numbers))

    # calculating the square of each number in numbers_excluding_negatives
    # then using sum function to calculate the sum of squares
    result = sum(list(map(lambda number: number * number, numbers_excluding_negatives)))

    # storing each sum of squares in a list
    results.append(result)


if __name__ == "__main__":
    main()
