import colorsys

def rotate(rgb, d):
    r, g, b = rgb
    d /= 360.
    h, l, s = colorsys.rgb_to_hls(r/255., g/255., b/255.)
    h = (h+d) % 1
    return tuple([int(round(i * 255.)) for i in colorsys.hls_to_rgb(h, l, s)])
    #print(final)
    #return tuple(final)

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

