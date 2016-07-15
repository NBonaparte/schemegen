# schemegen
simple, no-nonsense color scheme generator and config manager based on Charles Leifer/coleifer's [newer script](http://charlesleifer.com/blog/suffering-for-fashion-a-glimpse-into-my-linux-theming-toolchain/)

## Dependencies
* Python 3
* Python-Pillow

## Configuration
### Xresources
The `Xresources.template` creates an Xresources variables file, which will be imported in the main `~/.Xresources` file. Variables to be used in the main file are listed below.
### Templates
Template files should be put in `~/.config/schemegen/templates`. Examples are provided in the `templates` folder. Use the following variables to represent each color:

| Color         | Variable        | Xresources Variable |
|---------------|-----------------|---------------------|
| background    |`$bg`            |`bg`                 |
| foreground    | `$fg`           | `fg`                |
| black         | `$black`        | `black`             |
| red           | `$red`          | `red`               |
| green         | `$green`        | `green`             |
| yellow        | `$yellow`       | `yellow`            |
| blue          | `$blue`         | `blue`              |
| magenta       | `$magenta`      | `magenta`           |
| cyan          | `$cyan`         | `cyan`              |
| light gray    | `$lightgray`    | `lightgray`         |
| dark gray     | `$darkgray`     | `darkgray`          |
| light red     | `$lightred`     | `lightred`          |
| light green   | `$lightgreen`   | `lightgreen`        |
| light yellow  | `$lightyellow`  | `lightyellow`       |
| light blue    | `$lightblue`    | `lightblue`         |
| light magenta | `$lightmagenta` | `lightmagenta`      |
| light cyan    | `$lightcyan`    | `lightcyan`         |
| white         | `$white`        | `white`             |

Generated configs will be found in `~/.config/schemegen/configs`. It is recommended to symlink them to their default locations.
## Usage

### Accessing images
`schemegen.py -i [path/to/image]`

#### Number of colors sampled
Increasing the number of colors sampled can improve accuracy. The default is 64 and the maximum is 256.

`schemegen.py -i [path/to/image] -n 64`
### Reading color schemes
Schemegen can read Xresource files in `~/.config/schemegen/schemes`.

`schemegen.py -r [filename]`
### Printing to stdout
Along with writing to a Xresource scheme file in `~/.config/schemegen/schemes`, the scheme can also be output to stdout for easier copying.

`schemegen.py ... -p`
### Writing to configs
Schemegen can output configs in based on templates. See __Configuration__ for more info.

`schemegen.py ... -w`
