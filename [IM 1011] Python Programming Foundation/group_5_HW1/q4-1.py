### We give two ways to think about/ to solve this problem.
### 1. use inner product to determine which geometry the input point set belones.


#Q4
#given points on cartesian coordinate plane and determine the shape of the quadrilateral

points = input("please enter four points, eight numbers:")
pointlist = points.split(" ")
pointlist = [int(pointlist[i]) for i in range(len(pointlist))]

#points turning into length
x1 = pointlist[0] - pointlist[2]
y1 = pointlist[1] - pointlist[3]
x2 = pointlist[2] - pointlist[4]
y2 = pointlist[3] - pointlist[5]
x3 = pointlist[4] - pointlist[6]
y3 = pointlist[5] - pointlist[7]
x4 = pointlist[6] - pointlist[0]
y4 = pointlist[7] - pointlist[1]
length1 = (x1 * x1 + y1 * y1) ** 0.5
length2 = (x2 * x2 + y2 * y2) ** 0.5
length3 = (x3 * x3 + y3 * y3) ** 0.5
length4 = (x4 * x4 + y4 * y4) ** 0.5

#if lengths are different determine angles are right or not
if length1 != length2:
    dot = (pointlist[0] - pointlist[2]) * (pointlist[4] - pointlist[2]) + (pointlist[1] - pointlist[3]) * (pointlist[5] - pointlist[3])
    if dot == 0:
        print("rectangle", end='')
    else:
        print("others", end='')

#if lengths are same determine angles are right or not
if length1 == length2:
    dot = (pointlist[0] - pointlist[2]) * (pointlist[4] - pointlist[2]) + (pointlist[1] - pointlist[3]) * (pointlist[5] - pointlist[3])
    if dot == 0:
        print("square", end='')
    else:
        print("diamond", end='')


