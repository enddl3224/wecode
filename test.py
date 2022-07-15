def even():
    sum=0
    lst=[]

    for i in range(0,51,2):
        sum += i

    lst.append(sum)

    return lst

    
even()