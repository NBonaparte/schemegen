import hsluv

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

def rgb_to_hex(rgb):
    print("#%02x%02x%02x" % rgb)

