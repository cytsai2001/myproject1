### We give two ways to think about/ to solve this problem.
### 2. use slope to determine which geometry the input point set belones.

points = input('Type coordinates of four points x1, y1, x2, y2, x3, y3, x4, y4 in either clockwise or counter clockwise:(separating with spaces)')
pointslist = points.split(' ')

if len(pointslist) == 8:
    p1 = [float(pointslist[0]), float(pointslist[1])]
    p2 = [float(pointslist[2]), float(pointslist[3])]
    p3 = [float(pointslist[4]), float(pointslist[5])]
    p4 = [float(pointslist[6]), float(pointslist[7])]

    if p1 != p2 and p1 != p3 and p1 != p4 and p2 != p3 and p2 != p4 and p3 != p4:
        d12 = [a - b for a, b in zip(p2, p1)]
        d13 = [a - b for a, b in zip(p3, p1)]
        d14 = [a - b for a, b in zip(p4, p1)]
        d23 = [a - b for a, b in zip(p3, p2)]
        d24 = [a - b for a, b in zip(p4, p2)]
        d34 = [a - b for a, b in zip(p4, p3)]
        d41 = [a - b for a, b in zip(p1, p4)]

        cross1213 = d12[0]*d13[1]-d12[1]*d13[0]
        cross1314 = d13[0]*d14[1]-d13[1]*d14[0]
        cross1214 = d12[0]*d14[1]-d12[1]*d14[0]
        cross2324 = d23[0]*d24[1]-d23[1]*d24[0]

        if cross1213 == 0.0 or cross1214 == 0.0 or cross1314 == 0.0 or cross2324 == 0.0:
            print('collinear (others in the context of the description of the problem)', end='')

        elif cross1213 * cross1314 > 0.0:
            distance12 = d12[0] ** 2 + d12[1] ** 2
            distance23 = d23[0] ** 2 + d23[1] ** 2
            distance34 = d34[0] ** 2 + d34[1] ** 2
            distance41 = d41[0] ** 2 + d41[1] ** 2

            if d12[0] and d23[0] and d34[0] and d41[0] != 0.0:
                m12 = d12[1] / d12[0]
                m23 = d23[1] / d23[0]
                m34 = d34[1] / d34[0]
                m41 = d41[1] / d41[0]
                if m12 == m34 and m23 == m41 and m12 != m23:
                    if distance12 == distance23 == distance34 == distance41:
                        if m12 * m23 == -1.0:
                            print('square', end='')
                        else:
                            print('diamond', end='')
                    elif distance12 == distance34 and distance23 == distance41 and distance12 != distance23:
                        if m12 * m23 == -1.0:
                            print('rectangle', end='')
                        else:
                            print('others', end='')
                    else:
                        print('others', end='')
                else:
                    print('others', end='')
            elif d12[0] == d34[0] == 0.0:
                m23 = d23[1] / d23[0]
                m41 = d41[1] / d41[0]
                if distance12 == distance23 == distance34 == distance41:
                    if m23 == m41 == 0.0:
                        print('square', end='')
                    else:
                        print('diamond', end='')
                elif distance12 == distance34 and distance23 == distance41 and distance12 != distance23:
                    if m23 == m41 == 0.0:
                        print('rectangle', end='')
                    else:
                        print('others', end='')
                else:
                    print('others', end='')
            elif d23[0] == d41[0] == 0.0:
                m12 = d12[1] / d12[0]
                m34 = d34[1] / d34[0]
                if distance12 == distance23 == distance34 == distance41:
                    if m12 == m34 == 0.0:
                        print('square', end='')
                    else:
                        print('diamond', end='')
                elif distance12 == distance34 and distance23 == distance41 and distance12 != distance23:
                    if m12 == m34 == 0.0:
                        print('rectangle', end='')
                    else:
                        print('others', end='')
                else:
                    print('others', end='')
            else:
                print('others', end='')
        else:
            print('error: please type in clockwise or counter clockwise', end='')
    else:
        print('error: same points', end='')
else:
    print('error: wrong points numbers', end='')


