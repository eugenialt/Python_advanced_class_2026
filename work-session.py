data = [345,-890, 45, -9, 200, 657, 896]
# data = [-900, -999, 0, 456]

def rainfall_v1(data):
    maxnum = -999
    newarr = []
    for i in data :
        if i == maxnum:
            break
        if i >= 0:
            newarr.append(i)
        
    if len(newarr) > 0:
        avg = sum(newarr) / len(newarr)
        return avg
    else:
        return None
    

def rainfall_v2(data):
    i = 0
    n= 0
    sum = 0
    avg = 0
    while i < len(data):
        if data[i] >= 0:
            sum += data[i]
            n += 1
        elif i == -999  :
            break
        else:
            pass
        i += 1
    if n > 0:
        avg = sum/n
    return avg

def rainfall_v3(data):
    avg = [i>= 0 for i in data ]
    return avg

def rainfall_v3(data):
    i = 0
    newarr = []
    while i < len(data) and data[i] != -999:
        if data[i] >= 0:
            newarr.append(data[i])
        i += 1
    try:
        return sum(newarr) / len(newarr)
    except ZeroDivisionError:
        return 0
    
print(rainfall_v3(data))