if __name__ == "__main__":

    with open("input") as f:
        data = f.readlines()
    
    rhs = []
    lhs = []

    for row in data:
        rlhs, rrhs = row.split("   ")
        rhs.append(int(rrhs))
        lhs.append(int(rlhs))
    

    similarity = 0
    
    for r in rhs:
        if r in lhs:
            similarity += r
    
    print(similarity)