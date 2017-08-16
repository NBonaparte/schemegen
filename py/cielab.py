#_srgbGammaCorrInv = 0.03928/12.92
_srgbGammaCorrInv = 0.0031308
def rgb_to_xyz(rgb):
    r, g, b = (i/255. for i in rgb)
    r, g, b = [((v <= 0.03928) and [v / 12.92] or [((v+0.055) / 1.055) **2.4])[0] for v in (r, g, b)]
    print(r, g, b)
    # use the default sRGB reference white D65 2deg
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041
    return (x, y, z)

def xyz_to_cielab(xyz):
    return cielab

def rgb_to_cielab(rgb):
    return xyz_to_cielab(rgb_to_xyz(rgb))

def xyz_to_rgb(xyz):
    x, y, z = xyz
    r = x * 3.2404542 + y * -1.5371385 + z * -0.4985314
    g = x * -0.9692660 + y * 1.8760108 + z * 0.0415560
    b = x * 0.0556434 + y * -0.2040259 + z * 1.0572252
    print(r, g, b)
    #return tuple(int(round(i*255)) for i in [r, g, b])
    return tuple((((v <= _srgbGammaCorrInv) and [v * 12.92] or [(1.055 * (v ** (1/2.4))) - 0.055])[0] for v in (r, g, b)))


def cielab_to_xyz(cielab):
    return xyz

def cielab_to_rgb(cielab):
    return xyz_to_rgb(cielab_to_xyz(cielab))
