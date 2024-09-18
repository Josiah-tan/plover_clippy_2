# Plover\_clippy\_2

## Installation

### simple

  - To install this plugin, right click the plover icon. go to tools -\>
    plugins manager, find \`plover-clippy-2\`, and click
    "install/update".
  - When it finishes installing, restart Plover, go to configure -\>
    plugins, and check the box next to \`plover\_clippy\_2\` to activate
    the plugin

## File viewing

  - Now that you have installed this plugin it's time to use it\!
  - By default the output is written into clippy\_2.org in your config
    files
      - The same place as where your user.json and main.json is located

### Terminal

  - here are some live commands for different platforms

<!-- end list -->

1.  Windows
    
      - press start, type 'powershell' enter, then copy and paste the
        following:
    
    <!-- end list -->
    
    ``` bash
    Get-Content -path "$($env:LOCALAPPDATA)\plover\plover\clippy_2.org" -Wait -Tail 30
    ```

2.  Linux
    
    ``` bash
    tail -f clippy_2.org
    ```

3.  WSL
    
    Note that on WSL, the flag \`—disable-inotify\` may be required to
    make \`tail\` work
    
    ``` bash
    tail -f ---disable-inotify clippy_2.org
    ```

4.  Plover-live-view-nvim (neovim only)
    
      - This
        [plugin](https://github.com/Josiah-tan/plover-live-view-nvim) is
        a live viewer which supports:
          - Splits - You can split both horizontally and vertically and
            customize the sizes of the splits
          - Terminal viewing (requires
            [harpoon](https://github.com/ThePrimeagen/harpoon))

5.  vim-autoread (vim only \[no nvim\])
    
      - This [plugin](https://github.com/chrisbra/vim-autoread) is a
        live viewer for buffer viewing

6.  Extra
    
      - see [file viewing](docs.org::*file%20viewing) for more cool
        recipes

## Advanced

### Customization

  - In your config directory create a python file:
      - clippy\_2\_cfg.py
  - feel free to write all your customization code here\!

<!-- end list -->

1.  Initialization
    
      - Below are some states that can be set by the user
          - Note that these are the basic defaults (see [extended
            docs](docs.org::*Defaults) for more)
    
    <!-- end list -->
    
    ``` python
    def initPost(obj, clippy):
        clippy.state.output_file_name = "clippy_2.org"
        clippy.state.efficiency_symbol = "*"
        clippy.state.max_pad_efficiency = 5
        clippy.state.max_pad_english = 15
        clippy.state.justify = "left"
        clippy.state.last_num_translations = 10
    ```
    
      - output\_file\_name: name of the output file, directory location
        will default to config directory
      - efficiency\_symbol: any one character symbol used to denote how
        many strokes can be saved
      - max\_pad\_efficiency: the maximum number of efficiency symbols
        that are allowed to be displayed
      - max\_pad\_english: the maximum amount of space padding for
        English translations
      - justify: add white space either "left" or "right" to the output
      - last\_num\_translations: these number of translations are used
        to give suggestions
      - note: initPost executes after this plugin initializes itself

2.  Formatting Sources
    
      - The different formats come from different "sources", choose
        whenever you want\!\!\!
          - below is the default, but feel free to comment out whichever
            you want
    
    <!-- end list -->
    
    ``` python
    def startPost(obj, clippy):
        clippy.formatting.sources.set(
            ["Org", {"mode": "defaultSuggest"}]
            # ["Org", {"mode": "debugSuggest"}]
            # ["Org", {"mode": "minimalSuggest"}]
    
            # ["Retro", {"mode": "defaultSuggest"}]
            # ["Retro", {"mode": "minimalSuggest"}]
            )
    ```
    
      - For more information on customizing formatting sources, see the
        extended docs

3.  Suggestion sources
    
      - The suggestions come from different sources, and you can choose
        which sources to include\!\!\!
          - Listed below are the
    defaults
    
    <!-- end list -->
    
    ``` python
    clippy.translations.sources.set("Undo", "FingerSpelling", "Retro", "Tkfps")
    ```
    
      - see [Suggestion Sources](docs.org::*Suggestion%20Sources) for a
        more information on what each source does
      - see [Sources](docs.org::*Sources) for other methods like
        "append" and "prepend"

4.  distillation sources
    
      - TODO

5.  Extremity Sources
    
      - TODO

## Multiple configurations

  - In this plugin it is possible to use multiple configurations to do
    crazy things like:
      - multifile output, each with different configurations
          - for example one file could have syntax highlighting and the
            other doesn't
      - become a framework for other text output programs like
        tapey-tape (maybe in the future)
  - see [extended docs](docs.org::*Multiple%20Configurations) for more
    information
