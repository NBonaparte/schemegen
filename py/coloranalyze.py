from collections import OrderedDict
import math
import heapq
import colorsys  # stdlib
from PIL import Image
import harmony

def isolate_colors(filename, ncolors):
	img = Image.open(filename)
	if img.mode != 'RGB':
		img = img.convert('RGB')
	img = img.convert('P', palette=Image.ADAPTIVE, colors=ncolors)
	img = img.convert('RGB')
	return sorted(img.getcolors(ncolors), reverse=True)

# count_color is a sorted (desc) list of: [(pixel count, (r, g, b)), ...]
# rollup is the distance heuristic, arrived at by fiddling til it looked ok

def dedupe(count_color, rollup=10):
	result = {}
	for count, rgb in count_color:
		if rgb in result:
			result[rgb] += count
		else:
			for rrgb in result:
				dist = euclidean_dist(rrgb, rgb)
				#dist = harmony.hue_dist(rrgb, rgb)
				if dist < rollup:
					result[rrgb] += count
					break
			else:
				result[rgb] = count

	return sorted([(count, color) for color, count in result.items()], reverse=True)

def euclidean_dist(p1, p2):
	return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(3)))

canon_od =   OrderedDict([
        ("black", (0, 0, 0)),
        ("red", (255, 0, 0)),
        ("green", (0, 255, 0)),
        ("yellow", (255, 255, 0)),
        ("blue", (0, 0, 255)),
        ("magenta", (255, 0, 255)),
        ("cyan", (0, 255, 255)),
        ("lightgray", (192, 192, 192)),

        #("darkgray", (64, 64, 64)),
        #("lightred", (255, 128, 128)),
        #("lightgreen", (128, 255, 128)),
        #("lightyellow", (255, 255, 128)),
        #("lightblue", (128, 128, 255)),
        #("lightmagenta", (255, 128, 255)),
        #("lightcyan", (128, 255, 255)),
        #("white", (255, 255, 255))
])

def get_xcolors(colors, substitution_distance=20):
	results = []
	for crgb in canon_od.values():
		distances = []
		for rgb in colors:
			distance = euclidean_dist(crgb, rgb)
			#distance = harmony.hue_dist(crgb, rgb)
			heapq.heappush(distances, (distance, rgb))

		# First, try the closest RGB match.
		best = heapq.nsmallest(1, distances)[0][1]
		if best not in results:
			results.append(best)
		else:
			# Attempt to find a substitute.
			current = 0  # Distance from best color to potential substitute.
			min_dist = None
			vals = []
			while distances and current < substitution_distance:
				dist, rgb = heapq.heappop(distances)
				vals.append(rgb)

				# Here we're keeping an eye on the distance between
				# the potential substitute color, and the original
				# "best" color.
				if min_dist is None:
					min_dist = dist
				else:
					current = dist - min_dist

			for rgb in vals:
				if rgb not in results:
					# We found a substitute that isn't in use.
					results.append(rgb)
					break
			else:
				# No substitute found, just use the best match.
				results.append(vals[0])

	return results

def ensure_value(rgb, low, high):
	r, g, b = rgb
	h, s, v = colorsys.rgb_to_hsv(r / 256., g / 256., b / 256.)
	v = max(min(v, high), low)
	return tuple([i * 256. for i in colorsys.hsv_to_rgb(h, s, v)])

# Example, to ensure that black has a value between 0 and .2:
# fixed_black_rgb = ensure_value(black_rgb, 0.0, 0.2)


