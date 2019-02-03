from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from Turtle  import Turtle             # Import our Turtle
from Vector  import *                  # Import everything from our Vector

Turtle.m = 50.0                        # Scaling factor
Turtle.origin = Vector(400,300)
from Statue import *
from Mouse import *
from Cat import *

statue = Statue(Turtle.origin + Vector(0, 0),0)
mouse = Mouse(Turtle.origin + Vector(0, -Turtle.m).rotate(40),0)
cat = Cat(Turtle.origin + Vector(0, -4*Turtle.m).rotate(200),0, mouse)

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk, 800, 600)            # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen
arena.add(statue)                      # Add a very simple, statue
arena.add(mouse)                       # Add a green mouse centered at the base of the statue
arena.add(cat)                         # Add a red cat
cat_radius = StringVar()
cat_radius.set('CatRadius: %2.f' % cat.radius)
cat_angle = StringVar()
cat_angle.set('CatAngle: %2.f' % cat.angle)
mouse_angle = StringVar()
mouse_angle.set('MouseAngle: %2.f' % mouse.angle)
arena.add_labels(arena.time, cat_radius, cat_angle, mouse_angle)
tk.mainloop()                          # Enter the Tkinter event loop
