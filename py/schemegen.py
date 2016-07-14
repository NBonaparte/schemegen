#!/usr/bin/env python3
import string
import os
import argparse
import sys
from collections import OrderedDict
import coloranalyze
data_loc = os.path.expanduser("~") + "/.config/schemegen"

def colors(filename, num):
    # runs all functions in coloranalyze to obtain list of rgb tuples
    raw = coloranalyze.isolate_colors(filename, num)
    deduped = coloranalyze.dedupe(raw)
    cols = []
    for i in deduped:
        cols.append(i[1])
    xcols = coloranalyze.get_xcolors(cols)
    return xcols

def xres_out(hex_dict):
    # returns values in xresources format, useful for exporting to previewers like terminal.sexy
    final = ""
    i = 0
    for j, k in hex_dict.items():
        if j == "fg":
            final += "*.foreground: " + k + "\n"
        elif j == "bg":
            final += "*.background: " + k + "\n"
        else:
            final += "*.color" + str(i) + ": " + k + "\n"
            i += 1
    return final

def xres_parse(name):
    # parses xresources and returns list of colors
    xres_list = [None] * 18
    schemes = data_loc + "/schemes"
    with open(schemes + "/" + name, 'r') as f:
        for line in f.read().splitlines():
            if "*.color" in line:
                i = int(line.split()[0].replace("*.color", "").replace(":", ""))
                xres_list[i] = line.split()[-1]
            elif "*.background" in line:
                xres_list[16] = line.split()[-1]
            elif "*.foreground" in line:
                xres_list[17] = line.split()[-1]
    return xres_list

def rgb_to_hex(rgb):
    # converts list of rgb tuples to a list of hex values
    hexlist = []
    for i in rgb:
        hexlist.append("#%02x%02x%02x" % i)
    return hexlist

def scheme_write(hex_dict, pic_name):
    schemes = data_loc + "/schemes"
    os.makedirs(schemes, exist_ok=True)
    with open(schemes + "/" + pic_name, 'w') as f:
        f.write(xres_out(hex_dict))

def dict_gen(colors):
    # generates an ordered dictionary for config generator
    keylist = list(coloranalyze.canon_od.keys()) + ["bg", "fg"]
    d = OrderedDict(zip(keylist, colors))
    # if the dict doesnt include bg or fg, create them
    if "bg" not in d or "fg" not in d:
        d.update({"bg": d.get("black"), "fg": d.get("white")})
    return d

def config_gen(hex_dict):
    # creates a config file for every template in the templates directory
    templates = data_loc + "/templates"
    conf_dir = data_loc + "/configs"
    xres = os.path.expanduser("~") + "/.Xresources"
    xres_conf = conf_dir + "/Xresources"
    xres_string = "#include \"" + xres_conf + "\""
    os.makedirs(conf_dir, exist_ok=True)
    os.makedirs(templates, exist_ok=True)
    if not os.listdir(templates):
        print("Please create templates for configs in " + templates + ", and symlink original config locations to those in " + conf_dir + ".")
        sys.exit(0)
    for temp in os.listdir(templates):
        with open(templates + "/" + temp, 'r') as f:
            tmp = string.Template(f.read())
            subbed = tmp.safe_substitute(hex_dict)
        with open(conf_dir + "/" + os.path.splitext(temp)[0], 'w') as c:
            c.write(subbed)
    if os.path.isfile(xres_conf):
        with open(xres, 'r') as f:
            orig = f.read()
        if xres_string not in orig:
            with open(xres, 'w') as f:
                f.write(xres_string + "\n" + orig)
        print("Xresources updated, run xrdb ~/.Xresources to reload it")


def yes_no(question):
    # simple function returning yes/no boolean for stdin questions
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    elif reply[0] == 'n':
        return False
    else:
        print("Aborting...")
        return None

if __name__ == "__main__":
    #	    -option for reduced colors (0-7 equals 8-15) -> use diff canonical list or copy?
    parser = argparse.ArgumentParser(description="Color scheme generator and config manager based on coleifer's script")
    parse_img_scheme = parser.add_mutually_exclusive_group()
    parse_img_scheme.add_argument('-i','--image',  metavar='IMG', dest='image', type=str, help='path to image')
    parser.add_argument('-n', metavar='N', dest = 'ncol', type=int, help='number of sampled colors (higher = increased accuracy)', default=64)
    parser.add_argument('-w', '--write', dest='write', action='store_true', help='creates configs based on templates')
    parse_img_scheme.add_argument('-r', '--read', metavar='SCH', dest='read', type=str, help='get color scheme from file in scheme folder')
    parser.add_argument('-p', '--print', dest='print', action='store_true', help='prints scheme in Xresources format to stdout for copying')
    args = parser.parse_args()

    if args.read:
        try:
            hex_list = xres_parse(args.read)
        except OSError:
            print("Error: could not find scheme file")
    elif args.image:
        try:
            clist = colors(args.image, args.ncol)
            hex_list = rgb_to_hex(clist)
        except OSError:
            print("Error: could not find image")
    else:
        parser.print_help()
        sys.exit(0)
    hex_dict = dict_gen(hex_list)
    if args.image:
        scheme_write(hex_dict, os.path.splitext(os.path.basename(args.image))[0])
    if args.print:
        print(xres_out(hex_dict))
    if not args.write:
        sys.exit(0)
    else:
        if yes_no("Are you sure you want to overwrite configs?"):
            config_gen(hex_dict)
        else:
            sys.exit(0)
