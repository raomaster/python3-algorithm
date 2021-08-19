import random
import demos
import time


def create_random_list(size, max):
    ran_list = []
    for run in range(size):
        ran_list.append(random.randint(1, max))
    return ran_list

def analyze_fun(func_name, arr):
    tic = time.time()
    demos.quick_sort(l)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t -> Elapsed Time: {seconds}")


size = int(input("What size list do you want to create?"))
max = int(input("What is the mac value of the range?"))
run_times = int(input("How many times do you want to run?"))

# print(type(size), type(max))
# print(create_random_list(size, max))

for run in range(run_times):
    l = create_random_list(size, max)

    print(f"Run: {run+1}")
    print("List Created")

    # QuickSort Algorithm

    analyze_fun(demos.quick_sort, l.copy())

    # Merge Sort Algorithm
    analyze_fun(demos.merge_sort, l.copy())

    # Bubble Sort Algorithm
    analyze_fun(demos.bubble_sort, l.copy())

    # Python sortes Algorithm
    analyze_fun(sorted, l)

    print("-"*40)