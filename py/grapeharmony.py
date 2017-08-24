import harmony
import coloranalyze as ca

def getAll(rgb):
    new_colors = harmony.get_split_comp(rgb) + harmony.get_triad(rgb) + harmony.get_tetrad(rgb) + harmony.get_analog(rgb)
    #new_colors = harmony.get_triad(rgb)
    return new_colors

def getMoreLoop(rgb):
    colors = []
    for i in range(0, 12):
        colors.append(harmony.rotate(rgb, 30*i))
    return colors

def dist_key(a):
    return ca.euclidean_dist(a[0], ca.canon_od.get(a[1]))
def test_full(path):
    # do the normal stuff
    raw = ca.isolate_colors(path, 64)
    deduped = ca.dedupe(raw)
    cols = []
    for i in deduped:
        cols.append(i[1])
    xcols = ca.get_xcolors(cols)
    labeled = list(zip((ca.euclidean_dist(i, j) for i, j in zip(xcols, ca.canon_od.values())), xcols, ca.canon_od.keys()))
    #labeled = list(zip((harmony.hue_dist(i, j) for i, j in zip(xcols, ca.canon_od.values())), xcols, ca.canon_od.keys()))
    labeled.sort()
    # find the color that is closest to its canonical value which is not neutral
    labeled = [i for i in labeled if i[2] not in ["black", "darkgray", "lightgray", "white"]]
    print("picked " + labeled[0][2] + " to harmonize with: " + "#%02x%02x%02x" % labeled[0][1])
    #print("2nd " + labeled[1][2] + " to harmonize with: " + "#%02x%02x%02x" % labeled[1][1])
    #harmonized = getAll(labeled[0][1])
    harmonized = getMoreLoop(labeled[0][1])
    for i in harmonized:
        rgb_to_hex(i)
    print()
    combined = [i[1] for i in labeled] + list(harmonized)
    # add saturation filter?
    redux = [xcols[0], xcols[-1]]
    redux[1:1] = list(harmonized)
    #xcol_final = ca.get_xcolors(combined)
    xcol_final = ca.get_xcolors(redux)
    for i in xcol_final:
        rgb_to_hex(i)
    return xcol_final

def rgb_to_hex(rgb):
    print("#%02x%02x%02x" % rgb)

