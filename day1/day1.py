from time import perf_counter_ns
if __name__ == "__main__":
    # Get data
    t1 = perf_counter_ns()
    with open("input") as f:
        data = f.readlines()
    
    rhs = []
    lhs = []
    # split data and convert to int
    for row in data:
        rlhs, rrhs = row.split("   ")
        rhs.append(int(rrhs))
        lhs.append(int(rlhs))
    
    # Put both sides in order
    rhs.sort()
    lhs.sort()

    # Find the absolute value of the difference between each ordered row
    sum_of_difference = 0
    for i in range(len(lhs)):
        sum_of_difference += abs(rhs[i] - lhs[i])
    
    print(sum_of_difference)
    similarity = 0
    
    for r in rhs:
        if r in lhs:
            similarity += r
    
    print(similarity)

    t2 = perf_counter_ns()
    print((t2-t1)*10**-3)


