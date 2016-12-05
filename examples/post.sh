#!/bin/bash

# reload Xresources
xrdb ~/.Xresources
# reload dunst
pkill dunst
# set wallpaper if image path given
if  [ -z "$1" ]; then
	echo "No wallpaper given."
else
	nitrogen --set-zoom-fill "$1"
fi
