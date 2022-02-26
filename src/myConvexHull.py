from math import hypot

def jarak2titik(x1, x2):
    return hypot(x2[0]-x1[0], x2[1]-x1[1])

def kiriatas(x1, x2, x3):
    return x1[0]*x2[1] + x3[0]*x1[1] + x2[0]*x3[1] - x3[0]*x2[1] - x2[0]*x1[1] - x1[0]*x3[1] > 0

def kananbawah(x1, x2, x3):
    return x1[0]*x2[1] + x3[0]*x1[1] + x2[0]*x3[1] - x3[0]*x2[1] - x2[0]*x1[1] - x1[0]*x3[1] < 0