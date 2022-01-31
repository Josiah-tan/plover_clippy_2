Plover\_clippy\_2
=================

Installation
------------

-   Currently this plugin is not available in the official registry so
    you need to clone this repo

``` {.bash}
git clone https://github.com/Josiah-tan/plover_clippy_2 
```

-   cd into this repo
-   Then install for use!
    -   Note that \"plover\" is the executable that you downloaded to
        make Plover work in the first place
    -   See this
        [website](https://plover.readthedocs.io/en/latest/cli_reference.html)
        for the different locations depending on which platform you are
        using (Linux, Windows, etc)

``` {.bash}
cd plover_clippy_2
plover -s plover_plugins install -e .
```

-   Finally make sure to open plover, then go to configure, plugins and
    enable this plugin!

Usage
-----

### Basic

-   Now that you have installed this plugin it\'s time to use it!
-   By default the output is written into clippy\_2.org in your config
    files
    -   Basically the same place as where your user.json and main.json
        is

### Customization

-   In your config directory create a python file:
    -   clippy\_2\_cfg.py
-   Custom code in this section should be written into this file

1.  Initialization

    -   Below are some states that can be set by the user
        -   Note that these are the defaults

    ``` {.python}
    def initPost(obj, clippy):
        clippy.state.output_file_name = "clippy_2.org"
        clippy.state.efficiency_symbol = "*"
        clippy.state.max_pad_efficiency = 5
        clippy.state.max_pad_english = 15
    ```

    -   output\_file\_name: name of the output file, directory location
        will default to config directory
    -   efficiency\_symbol: any one character symbol used to denote how
        many strokes can be saved
    -   max\_pad\_efficiency: the maximum number of efficiency symbols
        that are allowed to be displayed
    -   max\_pad\_english: the maximum amount of space padding for
        English translations
    -   initPost executes after this plugin initializes itself

File viewing
------------

-   well obviously you can open up the file and take a look, but what if
    you want to have a live view while training?

### Terminal

-   here are some live commands for different platforms

1.  Windows

    ``` {.bash}
    Get-Content clippy_2.org -Wait -Tail 30
    ```

2.  Linux

    ``` {.bash}
    tail -f clippy_2.org
    ```

3.  WSL

    Note that on WSL, the flag \`---disable-inotify\` may be required to
    make \`tail\` work

    ``` {.bash}
    tail -f ---disable-inotify clippy_2.org
    ```

### Plover-live-view-nvim (neovim only)

-   This [plugin](https://github.com/Josiah-tan/plover-live-view-nvim)
    is a live viewer which supports:
    -   Splits - You can split both horizontally and vertically and
        customize the sizes of the splits
    -   Terminal viewing (requires
        [harpoon](https://github.com/ThePrimeagen/harpoon))
    -   Buffer viewing (requires
        [autoread-nvim](https://github.com/Josiah-tan/autoread-nvim))
        -   The benefit of this over the terminal is that you can use
            custom syntax highlighting!

### vim-autoread (vim only \[no nvim\])

-   This [plugin](https://github.com/chrisbra/vim-autoread) is a live
    viewer for buffer viewing

Dev
---

This section is for people who interested in improving this plugin!

### Installation

-   Get the latest build of plover

``` {.bash}
pip3 install plover==4.0.0.dev10
```

-   Fork this repo and clone it locally

``` {.bash}
git clone link/to/gitHub
```

-   cd into this repo
-   Then install for use!
    -   Note that \"plover\" is the executable that you downloaded to
        make Plover work in the first place
    -   See this
        [website](https://plover.readthedocs.io/en/latest/cli_reference.html)
        for the different locations depending on which platform you are
        using (Linux, Windows, etc)

``` {.bash}
cd plover_clippy_2
plover -s plover_plugins install -e .
```

-   Edit stuff, test it out and most of all, have fun!
-   Feel free to chuck me a pull request or raise an issue if you have
    any questions!
