
liste1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste2 = []
for i in liste1:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for x in j:
                    if type(x) == list:
                        for z in x:
                            liste2.append(z)
                    else:
                        liste2.append(x)
            else:
                liste2.append(j)
    else:
        liste2.append(i)
print(liste2)