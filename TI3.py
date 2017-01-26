import string

exclude = set(string.punctuation)
exclude.add(" ")
exclude.add(";")
d = 8
l2 = []
li = []
Y = []
p_z = []
p_x = []

plik = open('input1.txt', 'r')



for line in plik.readlines()[1:]:
    s = line
    Y.append(s[-2])
    l2 = s[0:-3].split() #.append(ch for ch in s[0:-1] if ch == '0' or '1')
    l2 = list(map(int, l2))
    li.append(l2)
Y = li[0]
li.remove(li[0])

plik.close()

print(li)

k = 0
sum_x = 0
sum_y = 0

#prawdopodobieństwa dla kolumn dla p(1)             zakomentowane - dla każdego X

for j in li:                            #for j in range(len(li[0])):
    for i in j:                        #for i in li
        sum_x += i                  #sum += i[j]
        k +=1
        pr_x = sum_x / k
    sum_x = 0
    k = 0
    p_x.append(pr_x)                    #p_z.append(pr_z)



k = 0
for i in Y:
    sum_y += i
    k += 1
    p_y = sum_y / k




H_X = 0
H_XY = 0

I = H_X - H_XY