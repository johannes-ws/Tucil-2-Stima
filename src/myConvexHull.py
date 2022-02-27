import numpy as np
from scipy import linalg

def kiri(p1, p2, p3):
    return p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1] > 0

def kanan(p1, p2, p3):
    return p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1] < 0

def jaraktitikkegaris(p1, p2, p3):
    return linalg.norm(np.cross(p2-p1, p1-p3)) / linalg.norm(p2-p1)

def area(p1, p2, p3):
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0)

def isInside(p1, p2, p3, p):
    A = area(p1, p2, p3)
    A1 = area(p, p2, p3)
    A2 = area(p1, p, p3)
    A3 = area(p1, p2, p)
    if (A == A1 + A2 + A3):
        return True
    else:
        return False

def divideandconquer(semua_bagian, bagian, titik1, titik2, solusi):
    global hull
    hull = solusi
    if (len(bagian) == 0):
        hull.append((titik1, titik2))
    elif (len(bagian) == 1):
        hull.append((titik1, bagian[0]))
        hull.append((bagian[0], titik2))
    else:
        global all_part
        global total_part
        global titiksampel

        jarakmaxtitikkegaris = 0
        titiksampel = bagian[0]
        for i in range(len(bagian)):
            jarak = jaraktitikkegaris(titik1, titik2, bagian[i])
            if (jarak >= jarakmaxtitikkegaris):
                jarakmaxtitikkegaris = jarak
                titiksampel = bagian[i]

        all_part = semua_bagian
        total_part = len(all_part)

        a = total_part
        all_part.append([])
        total_part += 1

        left = 0
        right = 0
        for i in range(len(bagian)):
            if (kiri(titik1, titiksampel, bagian[i])):
                left += 1
            elif (kanan(titik1, titiksampel, bagian[i])):
                right += 1
        if (left < right):
            for i in range(len(bagian)):
                if (kiri(titik1, titiksampel, bagian[i]) and not isInside(titik1, titiksampel, titik2, bagian[i])):
                    all_part[a].append(bagian[i])
        elif (left > right):
            for i in range(len(bagian)):
                if (kanan(titik1, titiksampel, bagian[i]) and not isInside(titik1, titiksampel, titik2, bagian[i])):
                    all_part[a].append(bagian[i])

        b = total_part
        all_part.append([])
        total_part += 1

        left = 0
        right = 0
        for i in range(len(bagian)):
            if (kiri(titiksampel, titik2, bagian[i])):
                left += 1
            elif (kanan(titiksampel, titik2, bagian[i])):
                right += 1
        if (left < right):
            for i in range(len(bagian)):
                if (kiri(titiksampel, titik2, bagian[i]) and not isInside(titik1, titiksampel, titik2, bagian[i])):
                    all_part[b].append(bagian[i])
        elif (left > right):
            for i in range(len(bagian)):
                if (kanan(titiksampel, titik2, bagian[i]) and not isInside(titik1, titiksampel, titik2, bagian[i])):
                    all_part[b].append(bagian[i])

        divideandconquer(all_part, all_part[a], titik1, titiksampel, hull)
        divideandconquer(all_part, all_part[b], titiksampel, titik2, hull)