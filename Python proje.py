
liste1 = [[1, 2], [3, 4], [5, 6, 7],8]
liste1 = liste1[:: -1]
liste2 = []
for i in liste1:
    if type(i) == list:
        i = i[:: -1]
        for j in i:
            liste2.append(j)
    else:
        liste2.append(i)
print(liste2)