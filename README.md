
# Table of Contents

1.  [Plover\_clippy\_2](#orgf4d6615)
    1.  [Installation](#org9022785)
        1.  [simple](#orgd35cceb)
        2.  [advanced](#org6a12fe3)
        3.  [developers](#org75e6657)
    2.  [Usage](#org557b6b7)
        1.  [Basic](#org61ee903)
        2.  [Customization](#org367a2f1)
    3.  [Multiple configurations](#org4aa5902)
    4.  [File viewing](#org8a50013)
        1.  [Terminal](#org0e73fb7)



<a id="orgf4d6615"></a>

# Plover\_clippy\_2


<a id="org9022785"></a>

## Installation


<a id="orgd35cceb"></a>

### simple

-   To install this plugin, right click the plover icon. go to tools -> plugins manager, find \`plover-clippy-2\`, and click &ldquo;install/update&rdquo;.
-   When it finishes installing, restart Plover, go to configure -> plugins, and check the box next to \`plover\_clippy\_2\` to activate the plugin


<a id="org6a12fe3"></a>

### advanced

-   To gain access to latest updates, you can alternatively install from [extended docs](docs.md)


<a id="org75e6657"></a>

### developers

-   If you are interested in contributing to this plugin, see [extended docs](docs.md)


<a id="org557b6b7"></a>

## Usage


<a id="org61ee903"></a>

### Basic

-   Now that you have installed this plugin it&rsquo;s time to use it!
-   By default the output is written into clippy\_2.org in your config files
    -   The same place as where your user.json and main.json is located


<a id="org367a2f1"></a>

### Customization

-   In your config directory create a python file:
    -   clippy\_2\_cfg.py
-   feel free to write all your customization code here!

1.  Initialization

    -   Below are some states that can be set by the user
        -   Note that these are the basic defaults (see [extended docs](docs.md) for more)
    
        def initPost(obj, clippy):
        	clippy.state.output_file_name = "clippy_2.org"
        	clippy.state.efficiency_symbol = "*"
        	clippy.state.max_pad_efficiency = 5
        	clippy.state.max_pad_english = 15
        	clippy.state.justify = "left"
        	clippy.state.last_num_translations = 10
    
    -   output\_file\_name: name of the output file, directory location will default to config directory
    -   efficiency\_symbol: any one character symbol used to denote how many strokes can be saved
    -   max\_pad\_efficiency: the maximum number of efficiency symbols that are allowed to be displayed
    -   max\_pad\_english: the maximum amount of space padding for English translations
    -   justify: add white space either &ldquo;left&rdquo; or &ldquo;right&rdquo; to the output
    -   last\_num\_translations: these number of translations are used to give suggestions
    -   note: initPost executes after this plugin initializes itself

2.  Formatting Sources

    -   The different formats come from different &ldquo;sources&rdquo;, choose whenever you want!!!
        -   below is the default, but feel free to comment out whichever you want
    
        def startPost(obj, clippy):
        	clippy.formatting.sources.set(
        		["Org", {"mode": "defaultSuggest"}]
        		# ["Org", {"mode": "debugSuggest"}]
        		# ["Org", {"mode": "minimalSuggest"}]
        
        		# ["Retro", {"mode": "defaultSuggest"}]
        		# ["Retro", {"mode": "minimalSuggest"}]
        		)
    
    -   For more information on customizing formatting sources, see the extended docs

3.  Suggestion sources

    -   The suggestions come from different sources, and you can choose which sources to include!!!
        -   Listed below are the defaults
    
        clippy.translations.sources.set("Undo", "FingerSpelling", "Retro", "Tkfps")
    
    -   see [Suggestion Sources](docs.md) for a more information on what each source does
    -   see [Sources](docs.md) for other methods like &ldquo;append&rdquo; and &ldquo;prepend&rdquo;

4.  distillation sources

    -   TODO

5.  Extremity Sources

    -   TODO


<a id="org4aa5902"></a>

## Multiple configurations

-   In this plugin it is possible to use multiple configurations to do crazy things like:
    -   multifile output, each with different configurations
        -   for example one file could have syntax highlighting and the other doesn&rsquo;t
    -   become a framework for other text output programs like tapey-tape (maybe in the future)
-   see [extended docs](docs.md) for more information


<a id="org8a50013"></a>

## File viewing

-   well obviously you can open up the file and take a look, but what if you want to have a live view while training?


<a id="org0e73fb7"></a>

### Terminal

-   here are some live commands for different platforms

1.  Windows

        Get-Content clippy_2.org -Wait -Tail 30

2.  Linux

        tail -f clippy_2.org

3.  WSL

    Note that on WSL, the flag \`&#x2014;disable-inotify\` may be required to make \`tail\` work
    
        tail -f ---disable-inotify clippy_2.org

4.  Plover-live-view-nvim (neovim only)

    -   This [plugin](https://github.com/Josiah-tan/plover-live-view-nvim) is a live viewer which supports:
        -   Splits - You can split both horizontally and vertically and customize the sizes of the splits
        -   Terminal viewing (requires [harpoon](https://github.com/ThePrimeagen/harpoon))

5.  vim-autoread (vim only [no nvim])

    -   This [plugin](https://github.com/chrisbra/vim-autoread) is a live viewer for buffer viewing

6.  Extra

    -   see [file viewing](docs.md) for more cool recipes

