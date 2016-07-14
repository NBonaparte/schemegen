# schemegen
simple, no-nonsense color scheme generator and config manager based on Charles Leifer/coleifer's [newer script](http://charlesleifer.com/blog/suffering-for-fashion-a-glimpse-into-my-linux-theming-toolchain/)

## Dependencies
* Python 3
* Pillow

## Configuration
Template files should be put in `~/.config/schemegen/templates`. Examples are provided in the `templates` folder. Use the following variables to represent each color:

| Color         | Variable      |
|---------------|---------------|
| background    |`$bg`            |
| foreground    | `$fg`           |
| black         | `$black`        |
| red           | `$red`          |
| green         | `$green`        |
| yellow        | `$yellow`       |
| blue          | `$blue`         |
| magenta       | `$magenta`      |
| cyan          | `$cyan`         |
| light gray    | `$lightgray`    |
| dark gray     | `$darkgray`     |
| light red     | `$lightred`     |
| light green   | `$lightgreen`   |
| light yellow  | `$lightyellow`  |
| light blue    | `$lightblue`    |
| light magenta | `$lightmagenta` |
| light cyan    | `$lightcyan`    |
| white         | `$white`        |

Generated configs will be found in `~/.config/schemegen/configs`. It is recommended to symlink them to their default locations.
### Xresources
The `Xresources.template` creates an Xresources variables file, which will be imported in the main `~/.Xresources` file. The variables for each color are listed in the template file (merely the same as above minus the `$`).
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
