import math
from PIL import Image
from PIL import ImageDraw

def binomial_coefficient(n, k):
    if k == 1: return n

    n_factorial = 1
    for x in range(1, n):
        n_factorial += n_factorial * x

    k_factorial = 1
    for x in range(1, k):
        k_factorial += k_factorial * x

    nk_factorial = 1
    for x in range(1, n - k):
        nk_factorial += nk_factorial * x

    return n_factorial/(k_factorial*nk_factorial)

def bernstein(n, i, t):
    return binomial_coefficient(n, i) * math.pow(t, i) * math.pow(1 - t, n - i)

def bezier_curve(points, steps):
    n = len(points) - 1
    result = []

    # calculate curve point for t
    def point(t):
        x = 0
        y = 0
        for i in range(0, n + 1):
            x += points[i][0] * bernstein(n,i,t)
            y += points[i][1] * bernstein(n,i,t)
        return (x, y)

    # steps for t from 0 to 1
    for x in range(0, steps+1):
        t = x * (1.0/steps)
        result.append( point(t) )
    
    return result

img_size = 475
img = Image.new("RGB", (img_size, img_size))
draw = ImageDraw.Draw(img)

draw.rectangle([0,0,img_size, img_size], fill="#fff")

m = [
    bezier_curve([(20, 400), (20, 20)], 100),
    bezier_curve([(20, 20), (120, 120)], 100),
    bezier_curve([(120, 120), (240, 20)], 100),
    bezier_curve([(240, 20), (240, 400)], 100),
]

for x in m:
    draw.line(x, fill="#000", width=2)

t = [
    bezier_curve([(270, 20), (450, 20)], 100),
    bezier_curve([(450, 20), (360, 20)], 100),
    bezier_curve([(360, 20), (360, 400)], 100),
]

for x in t:
    draw.line(x, fill="#000", width=2)

img.show()