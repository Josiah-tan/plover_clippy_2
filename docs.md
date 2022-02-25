# Alternative Installation

  - This section those how to install without using the plugin manager

<!-- end list -->

``` bash
git clone https://github.com/Josiah-tan/plover_clippy_2 
```

  - cd into this repo
  - Then install for use\!
      - Note that "plover" is the executable that you downloaded to make
        Plover work in the first place
      - See this
        [website](https://plover.readthedocs.io/en/latest/cli_reference.html)
        for the different locations depending on which platform you are
        using (Linux, Windows, etc)

<!-- end list -->

``` bash
cd plover_clippy_2
plover -s plover_plugins install -e .
```

  - Finally make sure to open plover, then go to configure, plugins and
    enable this plugin\!

# Defaults

  - below are all the defaults

<!-- end list -->

``` python
def initPost(obj, clippy):
    clippy.state.output_file_name = "clippy_2.org"
    clippy.state.efficiency_symbol = "*"
    clippy.state.max_pad_efficiency = 5
    clippy.state.max_pad_english = 15
    clippy.state.justify = "left"
    clippy.state.last_num_translations = 10

    clippy.state.colors = {
                    # for formatting
                    "suggestions": "neutral_aqua",
                    "stroked": "neutral_purple",
                    "english": "neutral_orange",
                    "efficiency_symbol": lambda efficiency_symbol: [
                            "bright_green", "bright_purple", "bright_blue",
                            "bright_orange", "bright_red"
                            ][min(len(efficiency_symbol.strip())-1, 4)],
                    "source": "gray",
                    # "*": "gray", # not implemented
                    # ">": "gray",
                    # for extremities
                    "START": "bright_green",
                    "STOP": "bright_red",
                    "date": "neutral_aqua",
                    # "-": "bright_blue",
                    }

    clippy.extremity.start_pre_sources.set(
                    ["Start", {
                            "colorscheme": "gruvbox",
                            "mode": "defaultPre"}])

    clippy.extremity.stop_pre_sources.set(
                    ["Stop", {
                            "colorscheme": "gruvbox",
                            "mode": "defaultPre"}])
```

  - colors: dictionary (key: value)
      - customizable keys (str): suggestions, stroked, english,
        efficiency\_symbol, source, START, END, date
      - customizable values, with several options:
          - color (str): listed in
            [gruvbox](plover_clippy_2/formatting/color/palletes/gruvbox.py)
          - hex RGB codes (str): of form "\#XXXXXX", such that X
            represents any value from 1 - F
          - ANSI escape codes, learn to make your own
            [here](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)
          - Function:
              - param: str, the actual value of the key used (e.g. see
                "efficiency\_symbol")
            <!-- end list -->
              - returns: color in any format
  - extremity: sources involving the start and end of the plugin life
      - See *Extremity Sources* for more information

# Formatting Sources

## Brief Description

  - customizable sources that can be utilized to generate output

## Builtin Features

  - currently the inbuilt "Retro" and "Org" classes have 3 parameters:
      - colorscheme: "gruvbox", currently the only colorscheme available
      - mode (str): there are several modes that you can choose (already
        shown in the readme)
      - colors (dict): overwrite colors from clippy.state.colors but
        only for this source

## Writing your own sources

  - Highly recommend checking out *sources* to see what you can do with
    it\!
  - feel free to check out [Retro](plover_clippy_2/formatting/retro.py)
    and [org](plover_clippy_2/formatting/org.py) for motivation, let us
    know on the plover discord if you need any help\!

# Sources

## Brief Description

  - A library for custom sources

## Methods

### Set

  - This method overrides any sources provided with a new list of
    sources

<!-- end list -->

1.  Examples
    
      - Here we pass a list of sources as strings for customizing the
        suggestions algorithm
    
    <!-- end list -->
    
    ``` python
    def startPost(obj, clippy):
        clippy.translations.sources.set("Undo", "FingerSpelling", "Retro", "Tkfps")
    ```
    
      - It is also possible to pass a list of sources as lists each
        containing the following:
          - a class or a string representing the name of the class
            (mandatory)
          - dictionary containing the keyword arguments for the class
            (optional)
          - iterable containing the arguments for the class (optional)
    
    <!-- end list -->
    
    ``` python
    def startPost(obj, clippy):
        clippy.distillations.sources.set(
                        ["Repeat", {"num": 1}],
                        ["Strokes", {"max": 3, "multi_max": 3}])
    ```

### Prepend

  - This method adds to the left of the list
      - Generally used for more "blocking" sources (makes more sense in
        the context of translation sources)

### Append

  - This method adds to the right of the list
      - Generally used for more "non-blocking" sources (makes more sense
        in the context of translation sources)

<!-- end list -->

1.  examples
    
      - This plugin also allows you to add your own classes in the
        configuration file\!
    
    <!-- end list -->
    
    ``` python
    class Beep:
        """
        beeps when you can save the at least "threshold" number of strokes
        """
    
        def __init__(self, threshold=1):
            self.threshold = threshold
    
        def beep(self):
            pass
            # TODO beeping here
    
        def distill(self, obj, clippy):
            stroked = clippy.state.phrase["stroked"]
            suggestions = clippy.state.phrase["suggestions"]
            for suggestion in suggestions:
                if len(stroked) - len(suggestion) >= threshold:
                    self.beep()
                    return True
            return True
    
    # append the source via the hook "startPost"
    def startPost(obj, clippy):
        # clippy.distillations.sources.append(
        #               [Beep, {"num": 1}])
      # or alternatively
        clippy.distillations.sources.append(
                        [Beep("num"=1)])
    ```
    
      - when writing your own sources, make sure to check back with the
        source code for reference (in this case
        [Repeat](plover_clippy_2/distillations/repeat.py) and
        [Strokes](plover_clippy_2/distillations/strokes.py)), because
        different sources have different requirements.

## Source Code

  - You can find the source code [here](plover_clippy_2/sources.py)

# Suggestion Sources

  - TODO

# Distillation Sources

  - TODO

# Extremity Sources

  - TODO

# Multiple Configurations

  - TODO

# File Viewing

## filtering

  - it turns out that you can use tools like 'grep' to filter
    suggestions out\!\!\!

### Grep

  - the code below will only show new rows write have two or more
    strokes saved:

<!-- end list -->

1.  windows
    
    ``` bash
    powershell.exe Get-Content clippy_2.org -Wait -Tail 30 | select-string '\*\*'
    ```

2.  Linux
    
    ``` bash
    tail -f clippy_2.org | grep -F '**'
    ```

## Highlighting

  - while there is builtin support for syntax highlighting, some people
    might be interested in this other option\!\!\!
  - one way to add additional highlighting is to use 'sed', for search
    and replace regular expressions

## Sed

Linux

  - here we replace \`\<\` with itself but colored pink

<!-- end list -->

``` bash
tail -f ---disable-inotify ~/.config/plover/clippy_2.org | sed -E 's/</\x1b[1;35m&\x1b[0m/g;'
```

# Developers

This section is for people who interested in improving this plugin\!

## Installation

  - Get the latest build of plover

<!-- end list -->

``` bash
pip3 install plover==4.0.0.dev10
```

  - Fork this repo and clone it locally

<!-- end list -->

``` bash
git clone link/to/gitHub
```

  - cd into this repo
  - Then install for use\!
      - Note that "plover" is the executable that you downloaded to make
        Plover work in the first place
      - See this
        [website](https://plover.readthedocs.io/en/latest/cli_reference.html)
        for the different locations depending on which platform you are
        using (Linux, Windows, etc)

<!-- end list -->

``` bash
cd plover_clippy_2
plover -s plover_plugins install -e .
```

  - Edit stuff, test it out and most of all, have fun\!
  - Feel free to chuck me a pull request or raise an issue if you have
    any questions\!
