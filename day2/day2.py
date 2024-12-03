import numpy as np
from time import perf_counter_ns
t1 = perf_counter_ns()
with open("./day2/input") as f:
    data = f.readlines()

data = [np.array(i.split(" "), dtype=np.float32) for i in data]


def row_safe(row:np.array)->bool:
    """
    Tells if a row is safe
    Args:
        row: an np.array containting the row
    """
    r = np.diff(row)
    if not (((np.abs(r)>3).any()) or ((r==0).any())):
        
        if (r<0).all():

            if (np.sign(r) == -1).all():
                return True
                # print("all negative",r,row.size)
                
        elif (r>0).all():

            if (np.sign(r) == 1).all():
                return True


safe = []
for row in data:
    r = np.diff(row)
    # print(r,row.size)
    if row_safe(row):
        safe.append(row)

print("Safe without problem dampener",len(safe))
safe = []
for row in data:
    r = np.diff(row)
    if row_safe(row):
        safe.append(row)
        # print("safe wo damp",row)
        
    elif (np.abs(r)>3).sum() + (r==0).sum() == 1:
        for i in range(row.size):
            rowmv = np.delete(row,i)
            if row_safe(rowmv):
                safe.append(rowmv)
                break
    else:
        for i in range(row.size):
            rowmv = np.delete(row,i)
            if row_safe(rowmv):
                safe.append(rowmv)
                break

print("Safe with problem dampener",len(safe))
t2 = perf_counter_ns()
print((t2-t1)*10**-6)