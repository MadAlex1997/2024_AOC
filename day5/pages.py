
# Get data
with open("day5/input") as w:
    r= w.readlines()

# Parse rules and order

rules = [i for i in r if "|" in i]

orders = [i for i in r if "," in i]

rules = [list(map(int,i.split("|"))) for i in rules]

orders = [list(map(int,i.split(","))) for i in orders]

midsum = 0
midsum_o_cor = 0
for ord in orders:
    ord_index = {o:i for i,o in enumerate(ord)}
    checklist=  []
    # Check if order follows rules
    for b, a in rules:
        if a in ord and b in ord:
            if ord_index[b]>ord_index[a]:
                checklist.append(False)
                break
            else:
                checklist.append(True)

    if all(checklist):
        midsum += ord[len(ord)//2]
    # If it doesn't
    else:
        rules_applicable = [i for i in rules if (i[0] in ord) and (i[1] in ord)]
        # Build a dictionary of page numbers and the number of times they have a dependency
        c_dict = dict()
        for rule in rules_applicable:
            if rule[1] not in c_dict.keys():
                c_dict[rule[1]] = 1
                if rule[0] not in c_dict.keys():
                    c_dict[rule[0]] = 0
            elif rule[0] not in c_dict.keys():
                c_dict[rule[0]] = 0
                c_dict[rule[1]] += 1
            else:
                c_dict[rule[1]] += 1
        
        order = list(c_dict.values())
        # Order the page numbers by the number of times they are a dependency
        new_ord = [o for c, o in sorted(zip(list(order),c_dict.keys()),key=lambda x:x[0]) ]
        # This works becuase it is the distance from the root page (zero dependencies) of the applicable rules
        # if the distance of the page from the root is the same they don't depend on eachother
        new_ord_index = {o:i for i,o in enumerate(new_ord)}
        
        # Check the new order and add the middle values
        checklist =  []
        for b, a in rules_applicable:
            if a in ord and b in ord:
                if new_ord_index[b]>new_ord_index[a]:
                    checklist.append(False)
                    break
                else:
                    checklist.append(True)
        if all(checklist):
            midsum_o_cor += new_ord[len(new_ord)//2]
        else:
            print("baaaaaaaaaaaaaaaaaaaaaaad")
                


print(midsum, midsum_o_cor)

