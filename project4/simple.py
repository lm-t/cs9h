from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen
turtle = Turtle(Vector(200, 200), 0)
arena.add(turtle)  # Add a very simple, basic turtle
tk.mainloop()                          # Enter the Tkinter event loop
