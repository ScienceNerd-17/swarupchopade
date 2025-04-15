import statistics

def compute_statistics(my_list):
    mean = statistics.mean(my_list)
    print("Mean: ", mean)

    median = statistics.median(my_list)
    print("Median: ", median)

    std_dev = statistics.stdev(my_list)
    print("Standard Deviation: ", std_dev)

    variance = statistics.variance(my_list)
    print("Variance: ", variance)

    correlation = statistics.correlation(my_list,your_list)
    print("Correlation: ", correlation)

my_list = input("Enter 20 numbers with space: ")
my_list = list(map(int, my_list.split()))

your_list = input("Enter 20 numbers with space: ")
your_list = list(map(int, your_list.split()))

if len(my_list) == 20:
    compute_statistics(my_list)
else:
    print("Number count exceeds 20.")