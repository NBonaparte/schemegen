import functools
from operator import methodcaller
from grapefruit import Color
import coloranalyze as ca
# closest to canonical, then get split complementary, triad, tetrad, analogous, monotone

def getAll(rgb):
    r, g, b = rgb
    orig = Color.NewFromRgb(r, g, b)
    new_colors = []
    # split complementary (150)
    new_colors.append(i.rgb for i in orig.TriadicScheme(150, 'rgb'))
    new_colors.append(i.rgb for i in orig.TriadicScheme(120, 'rgb'))
    new_colors.append(i.rgb for i in orig.TetradicScheme(30, 'rgb'))
    new_colors.append(i.rgb for i in orig.AnalogousScheme(30, 'rgb'))
    retlist = []
    for i in new_colors:
        for j in i:
            retlist.append((round(j[0]), round(j[1]), round(j[2])))
    return retlist

# remove light colors (only 8 in dict) so luminance can be determined later?
def test(rgb):
    cols = getAll(rgb)
    xcols = ca.get_xcolors(cols)
    distances = []
    smallest = 10000000 # lol
    for i, j in zip(xcols, ca.canon_od.values()):
        if ca.euclidean_dist(i, j) < smallest:
            smallest = ca.euclidean_dist(i, j)
            closest = i
        rgb_to_hex(i)
    return xcols

def comp_dist(a, b):
    if ca.euclidean_dist(a[0], ca.canon_od.get(a[1])) < ca.euclidean_dist(b[0], ca.canon_od.get(b[1])):
        return -1
    else:
        return 1
def dist_key(a):
    return ca.euclidean_dist(a[0], ca.canon_od.get(a[1]))
def test_full(path):
    # do the normal stuff
    raw = ca.isolate_colors(path, 256)
    deduped = ca.dedupe(raw)
    cols = []
    for i in deduped:
        cols.append(i[1])
    xcols = ca.get_xcolors(cols)
    #colors_labeled = list(zip(xcols, ca.canon_od.keys()))
    labeled = list(zip((ca.euclidean_dist(i, j) for i, j in zip(xcols, ca.canon_od.values())), ca.canon_od.keys()))
    print(labeled)
    # find the color that is closest to its canonical value, preferably not black/grey/white
    #return sorted(colors_labeled, key=functools.cmp_to_key(comp_dist))
    return sorted(labeled)

def rgb_to_hex(rgb):
    print("#%02x%02x%02x" % rgb)

