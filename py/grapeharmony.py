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

def test(rgb):
    cols = getAll(rgb)
    xcols = ca.get_xcolors(cols)
    return xcols

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
    labeled = list(zip((ca.euclidean_dist(i, j) for i, j in zip(xcols, ca.canon_od.values())), xcols, ca.canon_od.keys()))
    #print(labeled)
    # find the color that is closest to its canonical value, preferably not black/grey/white
    labeled.sort()
    labeled = [i for i in labeled if i[2] not in ["black", "lightgray"]]
    print("picked " + labeled[0][2] + " to harmonize with")
    rgb_to_hex(labeled[0][1])
    harmonized = test(labeled[0][1])
    #print(harmonized)
    combined = [i[1] for i in labeled] + harmonized
    xcol_final = ca.get_xcolors(combined)
    return xcol_final

def rgb_to_hex(rgb):
    print("#%02x%02x%02x" % rgb)

