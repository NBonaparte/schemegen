import hsluv
import math

def rotate(rgb, d):
    r, g, b = rgb
    h, s, l = hsluv.rgb_to_hsluv((r/255., g/255., b/255.))
    h = (h+d) % 360
    return tuple([int(round(i * 255.)) for i in hsluv.hsluv_to_rgb((h, s, l))])

def get_split_comp(rgb, d=150):
    a = rotate(rgb, d)
    b = rotate(rgb, -d)
    return (a, b)

def get_comp(rgb):
    return rotate(rgb, 180)

# combine triad and split_comp?
def get_triad(rgb, d=120):
    a = rotate(rgb, d)
    b = rotate(rgb, -d)
    return (a, b)

def get_tetrad(rgb, d=60):
    # testing with 120
    # arbitrary angle, default on grapefruit is 60deg
    a = get_comp(rgb)
    b = rotate(rgb, d)
    c = rotate(rgb, -(180-d))
    return (a, b, c)

# also combine?
def get_analog(rgb, d=30):
    a = rotate(rgb, d)
    b = rotate(rgb, -d)
    return (a, b)

def ensure_saturation(rgb, l, h):
    r, g, b = rgb
    h, s, l = hsluv.rgb_to_hsluv((r/255., g/255., b/255.))
    s = max(min(v, high), low)
    return tuple([int(round(i * 255.)) for i in hsluv.hsluv_to_rgb((h, s, l))])

def rgb_get_hue(rgb):
    r, g, b = rgb
    return hsluv.rgb_to_hsluv((r/255., g/255., b/255.))[0]

def hue_dist(c1, c2):
    return abs(rgb_get_hue(c1) - rgb_get_hue(c2))

def hsluv_dist(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    ch1 = hsluv.rgb_to_hsluv((r1/255., g1/255., b1/255.))
    ch2 = hsluv.rgb_to_hsluv((r2/255., g2/255., b2/255.))
    # this probably isn't the right way to calculate distance in cylindrical coordinates lol
    return math.sqrt(sum((ch1[i] - ch2[i]) ** 2 for i in range(3)))

def polar_dist(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    h1, s1, l1 = hsluv.rgb_to_hsluv((r1/255., g1/255., b1/255.))
    h2, s2, l2 = hsluv.rgb_to_hsluv((r2/255., g2/255., b2/255.))
    return math.sqrt(s1 ** 2 + s2 ** 2 - 2*s1*s2*math.cos(math.radians(h2) - math.radians(h1)))

def cyl_dist(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    # h = phi (angle), s = rho (radius), l = z
    h1, s1, l1 = hsluv.rgb_to_hsluv((r1/255., g1/255., b1/255.))
    h2, s2, l2 = hsluv.rgb_to_hsluv((r2/255., g2/255., b2/255.))
    x1 = s1 * math.cos(h1)
    x2 = s2 * math.cos(h2)
    y1 = s1 * math.sin(h1)
    y2 = s2 * math.sin(h2)
    #return math.sqrt(s1 ** 2 + s2 ** 2 - 2*s1*s2*math.cos(math.radians(h2) - math.radians(h1)))
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (l2 - l1) ** 2)

def rgb_to_hex(rgb):
    print("#%02x%02x%02x" % rgb)

