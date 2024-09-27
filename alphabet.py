def word(w):
    count= 0
    lst= []
    for i in w:
        if len(i) > 1 and i[0]==i[-1]:
            count= count+1
            prin