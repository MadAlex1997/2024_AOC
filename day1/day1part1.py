
if __name__ == "__main__":
    # Get data
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


