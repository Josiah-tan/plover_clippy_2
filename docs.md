
# Table of Contents

1.  [Alternative Installation](#org18e86a5)
2.  [Defaults](#org5e0be80)
3.  [Formatting Sources](#org9017e2a)
    1.  [Brief Description](#org2ee586a)
    2.  [Builtin Features](#org664c8fe)
    3.  [Writing your own sources](#org5ea422b)
4.  [Sources](#orgf017f83)
    1.  [Brief Description](#org3400bce)
    2.  [Methods](#orgd47a359)
        1.  [Set](#org18d1245)
        2.  [Prepend](#org46e5b52)
        3.  [Append](#orga1c28c1)
    3.  [Source Code](#org3485316)
5.  [Suggestion Sources](#orgf4234ca)
6.  [Distillation Sources](#org224b86d)
7.  [Extremity Sources](#org49189b7)
8.  [Multiple Configurations](#org06d65fa)
9.  [File Viewing](#orgebfa3db)
    1.  [filtering](#org39b2124)
        1.  [Grep](#org920fd4c)
    2.  [Highlighting](#orgeeb739c)
    3.  [Sed](#orgbd43817)
10. [Developers](#org12030c5)
    1.  [Installation](#org3b3c793)


<a id="org18e86a5"></a>

# Alternative Installation

-   This section those how to install without using the plugin manager

    git clone https://github.com/Josiah-tan/plover_clippy_2 

-   cd into this repo
-   Then install for use!
    -   Note that &ldquo;plover&rdquo; is the executable that you downloaded to make Plover work in the first place
    -   See this [website](https://plover.readthedocs.io/en/latest/cli_reference.html) for the different locations depending on which platform you are using (Linux, Windows, etc)

    cd plover_clippy_2
    plover -s plover_plugins install -e .

-   Finally make sure to open plover, then go to configure, plugins and enable this plugin!


<a id="org5e0be80"></a>

# Defaults

-   below are all the defaults

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

-   colors: dictionary (key: value)
    -   customizable keys (str): suggestions, stroked, english, efficiency<sub>symbol</sub>, source, START, END, date
    -   customizable values, with several options:
        -   color (str): listed in [gruvbox](plover_clippy_2/formatting/color/palletes/gruvbox.py)
        -   hex RGB codes (str): of form &ldquo;#XXXXXX&rdquo;, such that X represents any value from 1 - F
        -   ANSI escape codes, learn to make your own [here](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)
        -   Function:
            
            -   param: str, the actual value of the key used (e.g. see &ldquo;efficiency<sub>symbol</sub>&rdquo;)
            
            -   returns: color in any format
-   extremity: sources involving the start and end of the plugin life
    -   See [Extremity Sources](#org49189b7) for more information


<a id="org9017e2a"></a>

# Formatting Sources


<a id="org2ee586a"></a>

## Brief Description

-   customizable sources that can be utilized to generate output


<a id="org664c8fe"></a>

## Builtin Features

-   currently the inbuilt &ldquo;Retro&rdquo; and &ldquo;Org&rdquo; classes have 3 parameters:
    -   colorscheme: &ldquo;gruvbox&rdquo;, currently the only colorscheme available
    -   mode (str): there are several modes that you can choose (already shown in the readme)
    -   colors (dict): overwrite colors from clippy.state.colors but only for this source


<a id="org5ea422b"></a>

## Writing your own sources

-   Highly recommend checking out [sources](#orgf017f83) to see what you can do with it!
-   feel free to check out [Retro](plover_clippy_2/formatting/retro.py) and [org](plover_clippy_2/formatting/org.py) for motivation, let us know on the plover discord if you need any help!


<a id="orgf017f83"></a>

# Sources


<a id="org3400bce"></a>

## Brief Description

-   A library for custom sources


<a id="orgd47a359"></a>

## Methods


<a id="org18d1245"></a>

### Set

-   This method overrides any sources provided with a new list of sources

1.  Examples

    -   Here we pass a list of sources as strings for customizing the suggestions algorithm
    
        def startPost(obj, clippy):
        	clippy.translations.sources.set("Undo", "FingerSpelling", "Retro", "Tkfps")
    
    -   It is also possible to pass a list of sources as lists each containing the following:
        -   a class or a string representing the name of the class (mandatory)
        -   dictionary containing the keyword arguments for the class (optional)
        -   iterable containing the arguments for the class (optional)
    
        def startPost(obj, clippy):
        	clippy.distillations.sources.set(
        					["Repeat", {"num": 1}],
        					["Strokes", {"max": 3, "multi_max": 3}])


<a id="org46e5b52"></a>

### Prepend

-   This method adds to the left of the list
    -   Generally used for more &ldquo;blocking&rdquo; sources (makes more sense in the context of translation sources)


<a id="orga1c28c1"></a>

### Append

-   This method adds to the right of the list
    -   Generally used for more &ldquo;non-blocking&rdquo; sources (makes more sense in the context of translation sources)

1.  examples

    -   This plugin also allows you to add your own classes in the configuration file!
    
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
        	# 				[Beep, {"num": 1}])
          # or alternatively
        	clippy.distillations.sources.append(
        					[Beep("num"=1)])
    
    -   when writing your own sources, make sure to check back with the source code for reference (in this case [Repeat](plover_clippy_2/distillations/repeat.py) and [Strokes](plover_clippy_2/distillations/strokes.py)), because different sources have different requirements.


<a id="org3485316"></a>

## Source Code

-   You can find the source code [here](plover_clippy_2/sources.py)


<a id="orgf4234ca"></a>

# Suggestion Sources

-   TODO


<a id="org224b86d"></a>

# Distillation Sources

-   TODO


<a id="org49189b7"></a>

# Extremity Sources

-   TODO


<a id="org06d65fa"></a>

# Multiple Configurations

-   TODO


<a id="orgebfa3db"></a>

# File Viewing


<a id="org39b2124"></a>

## filtering

-   it turns out that you can use tools like &rsquo;grep&rsquo; to filter suggestions out!!!


<a id="org920fd4c"></a>

### Grep

-   the code below will only show new rows write have two or more strokes saved:

1.  windows

        powershell.exe Get-Content clippy_2.org -Wait -Tail 30 | select-string '\*\*'

2.  Linux

        tail -f clippy_2.org | grep -F '**'


<a id="orgeeb739c"></a>

## Highlighting

-   while there is builtin support for syntax highlighting, some people might be interested in this other option!!!
-   one way to add additional highlighting is to use &rsquo;sed&rsquo;, for search and replace regular expressions


<a id="orgbd43817"></a>

## Sed

1.  Linux

    -   here we replace \`<\` with itself but colored pink
    
        tail -f ---disable-inotify ~/.config/plover/clippy_2.org | sed -E 's/</\x1b[1;35m&\x1b[0m/g;'


<a id="org12030c5"></a>

# Developers

This section is for people who interested in improving this plugin!


<a id="org3b3c793"></a>

## Installation

-   Get the latest build of plover

    pip3 install plover==4.0.0.dev10

-   Fork this repo and clone it locally

    git clone link/to/gitHub

-   cd into this repo
-   Then install for use!
    -   Note that &ldquo;plover&rdquo; is the executable that you downloaded to make Plover work in the first place
    -   See this [website](https://plover.readthedocs.io/en/latest/cli_reference.html) for the different locations depending on which platform you are using (Linux, Windows, etc)

    cd plover_clippy_2
    plover -s plover_plugins install -e .

-   Edit stuff, test it out and most of all, have fun!
-   Feel free to chuck me a pull request or raise an issue if you have any questions!

