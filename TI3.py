import string
from math import log2

exclude = set(string.punctuation)
exclude.add(" ")
exclude.add(";")
d = 6
file = 'input.txt'
l2 = []
li = []
Y = []             # odwrotny wybór
P_x = []
pr_x = 0
p_y = 0
zi = []
Z = []
I = []
Izz = []

plik = open(file, 'r')

for line in plik.readlines()[1:]:
    s = line
    Y.append(s[-2])                # odwrotny wybór
    l2 = s[0:-3].split()
    l2 = list(map(int, l2))
    li.append(l2)
# Y = li[0]                       #odwrotny wybór
Y = list(map(int, Y))
# li.remove(li[0])

plik.close()

k = 0
sum_x = 0
sum_y = 0

# prawdopodobieństwa dla kolumn dla p(1)             zakomentowane - dla każdego X

for j in range(len(li[0])):                            # for j in li:
    for i in li:                        # for i in j
        sum_x += i[j]                   # sum += i
        zi.append(i[j])                 # tworzę wektor dla cechy
        k += 1
        pr_x = sum_x / k
    P_x.append(pr_x)                    # tabelka prawdopodobieństw dla kolejnych ixów           # p_x.append(pr_x)
    Z.append(zi)                           # tworzę tablicę, gdzie cechy są poziomo (transpozycja wejściowej)
    zi = []
    sum_x = 0
    k = 0

for i in Y:
    sum_y += i
    k += 1
    p_y = sum_y / k

P_y = p_y


dct = {'00': 0, '01': 0, '10': 0, '11': 0}
dctZZ = {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 0}
l_dct = []
l_zz = []
l_zzy = []
l_l_zz = []
l_dctZZ = []
for j in Z:

    l_dct.append(dict(dct))
    l_dctZZ.append(dict(dctZZ))

m = 0
n = 0
for j in Z:
    # dla każdej cechy liczymy informację wspólną z etykietami
    n = 0
    for i in j:
        yy = Y[n]
        x = str(i)
        ky = x + str(yy)
        n += 1
        l_dct[m][ky] += 1
    m += 1



N = n       #ilosc wektorów X, nie cech
q = 0
for i in Z:
    px00 = l_dct[q]['00'] / N           # to jest prawdopodobieństrwo, że p(x,y) x=0, y=0
    px01 = l_dct[q]['01'] / N
    px10 = l_dct[q]['10'] / N
    px11 = l_dct[q]['11'] / N
    px0 = 1 - P_x[q]
    px1 = P_x[q]
    py0 = 1 - P_y
    py1 = P_y

    x0y0 = px00 * log2(px00/(px0 * py0))
    x0y1 = px01 * log2(px01/(px0 * py1))
    x1y0 = px10 * log2(px10/(px1 * py0))
    x1y1 = px11 * log2(px11/(px1 * py1))
    Ii = x0y0 + x0y1 + x1y0 + x1y1
    I.append(Ii)
    q += 1

i1 =max(I)
Z1_ind = I.index(i1)
Z1 = Z[Z1_ind]

Zi = []
Zi.append(Z1)
mm = 0
f = 0

while f <= d:

    for p in Zi:
        mm = 0
        print(p)
        for j in Z:
            l_zz.append(dict(dct))
            # dla każdej pary cech liczymy informację prawdopodobieństwo wystąpienia par
            # n = 0
            for i in j:
                # yy = Y[n]
                x = str(p[i]) + str(i)
                # ky = x + str(yy)
                # n += 1
                l_zz[mm][x] += 1           # wystąpienia par zapisane w slowniku, nowe "p_x", prawdopodobieństwa trójek potem
            mm += 1
        print(l_zz)
        print(len(l_zz))
        l_l_zz.append(l_zz)
        l_zz = []
        f += 1

    # ogarnąć trójki (poniżej) !
    mm = 0
    q = 0
    for p in Zi:
        l_zzy.append(dict(dctZZ))
        for j in Z:
            # dla każdej pary cech liczymy informację prawdopodobieństwo wystąpienia par
            n = 0
            for i in j:
                yy = Y[n]
                x = str(i) + str(yy)
                ky = x + str(yy)
                n += 1
                l_zzy[-1][ky] += 1  # wystąpienia trójek zapisane w slowniku, nowe "p_xy"
            mm += 1

            P_z = [] # prawdopodobieństwo wystąpienia trójki

    for i in Z:                                 # ogarnąć TRÓJKI
        px000 = l_zzy[q]['000'] / N             # to jest p(x,y), że x1=0, x2 = 0, y=0
        px001 = l_zzy[q]['001'] / N
        px010 = l_zzy[q]['010'] / N
        px011 = l_zzy[q]['011'] / N
        px100 = l_zzy[q]['100'] / N
        px101 = l_zzy[q]['101'] / N
        px110 = l_zzy[q]['110'] / N
        px111 = l_zzy[q]['111'] / N

        pzz00 = 1 - P_z[q]
        pzz01 = P_z[q]
        pzz10 = 1 - P_z[q]
        pzz11 = P_z[q]
        py0 = 1 - P_y
        py1 = P_y

        x00y0 = px00 * log2(px00 / (pzz00 * py0))
        x00y1 = px01 * log2(px01 / (pzz00 * py1))
        x01y0 = px10 * log2(px10 / (pzz01 * py0))
        x01y1 = px11 * log2(px11 / (pzz01 * py1))
        x10y0 = px00 * log2(px00 / (pzz10 * py0))
        x10y1 = px01 * log2(px01 / (pzz10 * py1))
        x11y0 = px10 * log2(px10 / (pzz11 * py0))
        x11y1 = px11 * log2(px11 / (pzz11 * py1))
        Iz = x00y0 + x00y1 + x01y0 + x01y1 + x10y0 + x10y1 + x11y0 + x11y1
        Izz.append(Iz)
        q += 1

    iz = max(Izz)
    iz_ind = Izz.index(i1)
    Zn = Z[iz_ind]     # to ma być wiersz, który "wybieram"
    Zi.append(Zn)



