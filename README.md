#GraphEditor

Simple graphic editor CLI to learn python

##Commands

```
C <name> <x> <y> <radius>       # Add a circle
R <name> <x1> <y1> <x2> <y2>    # Add a rectangle
L <name> <x1> <y1> <x2> <y2>    # Add a line
PL <name> <x1> <y1> <x2> <y2>   # Add a polyline
OA <name1> [name2...]           # Create an agregated object with existing objects
DELETE <name1> [name2...]       # Delete selected objects
MOVE <name> <x> <y>             # Move the position of the selected element
LIST                            # Enumerate all the exsiting elements
UNDO                            # UNDO last command
REDO                            # Redo the privious UNDO
LOAD <filename>                 # Load a saved canvas
SAVE <filename>                 # Save an existing canvas
CLEAR                           # Clear all the elements from the canvas
EXIT                            # Exit the app
```

If comand success to execute the result is displayed on the console.
In the other case `#ERR` is printed followed by the considered error
