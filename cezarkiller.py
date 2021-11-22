alfa = 'abcdefghijklmnopqrstuvwxyz'
polHist = [
    0.099,
    0.0147,
    0.0436,
    0.0325,
    0.0877,
    0.003,
    0.0142,
    0.0108,
    0.0821,
    0.0228,
    0.0351,
    0.0392,
    0.028,
    0.0572,
    0.086,
    0.0313,
    0.0014,
    0.0469,
    0.0498,
    0.0398,
    0.025,
    0.0004,
    0.0465,
    0.0002,
    0.0376,
    0.0653
]

inwokacja = "Litwo! Ojczyzno moja! Ty jesteś jak zdrowie, Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie Panno święta, co Jasnej bronisz Częstochowy I w Ostrej świecisz Bramie! Ty, co gród zamkowy Nowogródzki ochraniasz z jego wiernym ludem! Jak mnie dziecko do zdrowia powróciłaś cudem, (Gdy od płaczącej matki pod Twoją opiekę Ofiarowany, martwą podniosłem powiekę I zaraz mogłem pieszo do Twych świątyń progu Iść za wrócone życie podziękować Bogu), Tak nas powrócisz cudem na Ojczyzny łono. Tymczasem przenoś moją duszę utęsknioną Do tych pagórków leśnych, do tych łąk zielonych, Szeroko nad błękitnym Niemnem rozciągnionych; Do tych pól malowanych zbożem rozmaitem, Wyzłacanych pszenicą, posrebrzanych żytem; Gdzie bursztynowy świerzop, gryka jak śnieg biała, Gdzie panieńskim rumieńcem dzięcielina pała, A wszystko przepasane jakby wstęgą, miedzą Zieloną, na niej z rzadka ciche grusze siedzą."
prepare = lambda s: s.lower().replace(",","").replace(".","").replace(";","").replace("!","").replace("?","").replace("ą","a").replace("ę","e").replace("ć","c").replace("ł","l").replace("ń","n").replace("ó","o").replace("ś","s").replace("ź","z").replace("ż","z").replace(" ","").replace("(","").replace(")","")
inwo = prepare(inwokacja)

def maxindex(l): return l.index(max(l))
def minindex(l): return l.index(min(l))

def listprint(l):
    print('[')
    for v in l:
        print(f'\t{v}')
    print('\t]')

def szyfr(s, d=3):
    """
    Args:
    s (String) - tekst jawny.
    d (int) - przesunięcie (domyślnie 3 - szyfr cezara)

    returns:
    szyfrogram (String)
    """

    w = ''
    for l in s:
        # print(l, end="")
        w+=alfa[(alfa.index(l)+d)%len(alfa)]
    return w

def histogram(s):
    """
    """
    h = [0]*len(alfa)
    for (k, v) in enumerate(s):
        h[alfa.index(v)]+=1
    return list(map(lambda x: x/len(s), h))

def getShiftFromMSE(l, m):
    """
    l do porównania z m
    (jak l jest większy, wynik jest dodatni, czyli m+d=l)

    Args:
    l (iterable[float]) - wynik otrzymany
    m (iterable[float]) - wynik oczekiwany

    returns:
    shift (int) - przesunięcie, dla którego wynik MSE jest najmniejszy
    """
    diffs = []
    for shift in range(len(l)):
        diffs.append(list(map(lambda i: m[i]-l[(i+shift)%len(l)], range(len(l)))))
    MSE = []
    for shift in range(len(l)):
        MSE.append(sum(map(lambda x: x**2, diffs[shift])))
    # listprint(MSE)
    return minindex(MSE)

def getShiftFromMAX(l, m):
    """
    l do porównania z m
    (jak l jest większy, wynik jest dodatni, czyli m+d=l)

    Args:
    l (iterable[float]) - wynik otrzymany
    m (iterable[float]) - wynik oczekiwany

    returns:
    shift (int) - przesunięcie, dla którego pozycja najwyższego słupka się zgadza
    """
    return maxindex(l)-maxindex(m)

def deszyfrMSE(s):
    hist = histogram(s)
    d = getShiftFromMSE(hist, polHist)
    return szyfr(s, -1*d)
    


# print(szyfr(inwo))
hist = histogram(inwo)
# print(hist)
# print(polHist)
print(getShiftFromMSE(hist, polHist))
print(getShiftFromMAX(hist, polHist))
print(deszyfrMSE(szyfr(inwo)))

