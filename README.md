# schemegen
simple, no-nonsense color scheme generator and config manager based on Charles Leifer/coleifer's [newer script](http://charlesleifer.com/blog/suffering-for-fashion-a-glimpse-into-my-linux-theming-toolchain/)

## Installation
### Dependencies
* Python 3
* Python-Pillow
* [HSLuv](http://www.hsluv.org/) Python implementation

### Packages
For Arch Linux users, an AUR package is available as [schemegen-git](https://aur.archlinux.org/packages/schemegen-git/).

## Configuration
### Xresources
The `Xresources.template` creates an Xresources variables file, which will be imported in the main `~/.Xresources` file.
This line will be inserted into your Xresources if not already there, to link to the variable file:
```
#include "$HOME/.config/schemegen/configs/Xresources"
```

Variables to be used in the main file are listed below.
### Templates
Template files should be put in `~/.config/schemegen/templates`, and should have the extension `.template`. Examples are provided in the `templates` folder. Use the following variables to represent each color:

| Color         | Variable         |  Variable (no `#`) |Xresources Variable |
|---------------|------------------|--------------------|--------------------|
| background    | `%bg%`           |  `%@bg%`           |`bg`                |
| foreground    | `%fg%`           |  `%@fg%`           |`fg`                |
| black         | `%black%`        |  `%@black%`        |`black`             |
| red           | `%red%`          |  `%@red%`          |`red`               |
| green         | `%green%`        |  `%@green%`        |`green`             |
| yellow        | `%yellow%`       |  `%@yellow%`       |`yellow`            |
| blue          | `%blue%`         |  `%@blue%`         |`blue`              |
| magenta       | `%magenta%`      |  `%@magenta%`      |`magenta`           |
| cyan          | `%cyan%`         |  `%@cyan%`         |`cyan`              |
| light gray    | `%lightgray%`    |  `%@lightgray%`    |`lightgray`         |
| dark gray     | `%darkgray%`     |  `%@darkgray%`     |`darkgray`          |
| light red     | `%lightred%`     |  `%@lightred%`     |`lightred`          |
| light green   | `%lightgreen%`   |  `%@lightgreen%`   |`lightgreen`        |
| light yellow  | `%lightyellow%`  |  `%@lightyellow%`  |`lightyellow`       |
| light blue    | `%lightblue%`    |  `%@lightblue%`    |`lightblue`         |
| light magenta | `%lightmagenta%` |  `%@lightmagenta%` |`lightmagenta`      |
| light cyan    | `%lightcyan%`    |  `%@lightcyan%`    |`lightcyan`         |
| white         | `%white%`        |  `%@white%`        |`white`             |

Note that the `@` symbol can be prepended to the variable to prevent the final color string from including `#` (`#fff -> fff`).

Generated configs will be found in `~/.config/schemegen/configs`. It is recommended to symlink them to their default locations.
### Post-install script
A post-install script can be added at `~/.config/schemegen/post.sh`. It will be run after writing to configs, and is useful for commands like `xrdb ~/.Xresources`. The path of the image sampled or found in the scheme file will be passed as an argument, if available. The user should have permission to execute the file (`chmod +x [FILE]`).

See the example [post.sh](examples/post.sh) for reference.
## Usage
Schemegen reads or generates a color scheme, creates a scheme file in `~/.config/schemegen/schemes/generated/`, and writes config files (upon user approval) by default. Options can be found below.

### Generating a color scheme based on an image
Schemegen can generate a color scheme based on a specified image, picking colors closest to the canonical scheme (see coleifer's [blog post](http://charlesleifer.com/blog/suffering-for-fashion-a-glimpse-into-my-linux-theming-toolchain/)).

`schemegen -i [path/to/image]`

#### Number of colors sampled
Increasing the number of colors sampled can improve accuracy. The default is 64 and the maximum is 256.

`schemegen -i [path/to/image] -n 64`
### Reading color schemes
Schemegen can use existing schemes (made by itself or placed by the user) by reading from Xresource files in `~/.config/schemegen/schemes`.

`schemegen -r [filename]`
### Listing all color schemes
All schemes found in `~/.config/schemegen/schemes` and their colors will be shown in a list.

`schemegen -l`
### Printing to stdout
Along with writing to a Xresource scheme file in `~/.config/schemegen/schemes/generated/`, the scheme can also be output to stdout for easier copying.

`schemegen ... -p`
### Writing to configs
Schemegen requests for user permission to write (and replace) configs. The `-f` option can be used to skip the overwriting dialog and force the config files to be overwritten.
