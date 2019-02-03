from Tkinter import *
from Turtle  import Turtle
from Vector  import *
from math import sin, cos, pi, sqrt
from cmath import acos
from Color import *

Turtle.m = 50.0                        # Scaling factor
Turtle.origin = Vector(400,300)

class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    def __init__(self, parent, width=400, height=400, **options):
        Frame.__init__(self, parent, **options)
        self.width, self.height = width, height
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()
        self.parent = parent
        parent.title("Project 5 - CS9H Turtle Arena")
        Button(self, text='reset', command=self.reset).pack(side=LEFT)
        Button(self, text='step', command=self.step).pack(side=LEFT)
        Button(self, text='run', command=self.run).pack(side=LEFT)
        Button(self, text='stop', command=self.stop).pack(side=LEFT)
        Button(self, text='quit', command=parent.quit).pack(side=LEFT)
        #
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="About...", command=self.about)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        parent.config(menu=menubar)
        #
        self.t = 0
        self.time = StringVar()
        self.time.set('Time: %d min.' % self.t)
        self.cat_radius = StringVar()
        self.cat_angle = StringVar()
        self.mouse_angle = StringVar()
        #
        self.checkvar = IntVar()
        chkbtn = Checkbutton(self, text="clockwise", variable=self.checkvar, onvalue=1, offvalue=0)
        chkbtn.pack(side = BOTTOM)
        #
        self.turtles = []
        self.items = {}
        self.running = 0
        self.period = 10 # milliseconds
        self.canvas.bind('<ButtonPress>', self.press)
        self.canvas.bind('<Motion>', self.motion)
        self.canvas.bind('<ButtonRelease>', self.release)
        self.dragging = None

    def press(self, event):
        dragstart = Vector(event.x, event.y)
        for turtle in self.turtles:
            if (dragstart - turtle.position).length() < 10:
                self.dragging = turtle
                self.dragstart = dragstart
                self.start = turtle.position
                return

    def motion(self, event):
        drag = Vector(event.x, event.y)
        if self.dragging:
            self.dragging.position = self.start + drag - self.dragstart
            self.update(self.dragging)

    def release(self, event):
        self.dragging = None

    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self.items[turtle]
        vertices = [(v.x, v.y) for v in turtle.getshape()]
        self.canvas.coords(item, sum(vertices, ()))
        self.canvas.itemconfigure(item, **turtle.style)

    def add(self, turtle):
        """Add a new turtle to this arena."""
        self.turtles.append(turtle)
        self.items[turtle] = self.canvas.create_polygon(0, 0)
        self.update(turtle)

    def step(self, stop=1):
        """Advance all the turtles one step."""
        self.t += 1
        self.time.set('Time: %d min.' % self.t)
        nextstates = {}
        for turtle in self.turtles:
            nextstates[turtle] = turtle.getnextstate()
        for turtle in self.turtles:
            turtle.setstate(nextstates[turtle])
            self.update(turtle)
            if isinstance(turtle, Cat):
                self.cat_radius.set('CatRadius: %2.f' % turtle.radius)
                self.cat_angle.set('CatAngle: %2.f' % turtle.angle)
            elif isinstance(turtle, Mouse):
                self.mouse_angle.set('MouseAngle: %2.f' % turtle.angle)
        if stop:
            self.running = 0

    def run(self):
        """Start the turtles running."""
        self.running = 1
        self.loop()

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(0)
        if self.running:
            self.tk.createtimerhandler(self.period, self.loop)

    def stop(self):
        """Stop the running turtles."""
        self.running = 0

    def reset(self):
        self.destroy()
        initialize()

    def add_labels(self, time, cat_radius, cat_angle, mouse_angle):
        """Add labels to the window that displays useful information"""
        Label(self, textvariable = mouse_angle).pack(side = RIGHT)
        Label(self, textvariable = cat_angle).pack(side = RIGHT)
        Label(self, textvariable = cat_radius).pack(side = RIGHT)
        Label(self, textvariable = time).pack(side = RIGHT)

    def about(self):
       filewin = Toplevel(self.parent)
       filewin.title("About the UC Berkeley CS9H Turtle Arena")
       photo = PhotoImage(file='photo.gif')
       text = Label(filewin, text="My name is Luis and this is project 5 'Turtle Arena'.")
       text.pack()
       pic = Label(filewin, image=photo)
       pic.photo = photo
       pic.pack()
       button = Button(filewin, text="Ok", command=filewin.destroy)
       button.pack()

class Statue(Turtle):
    """docstring for Statue"""
    def __init__(self, position, heading, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
    def getshape(self):
        forward = unit(self.heading)
        return [self.position + (forward*self.m).rotate(x) for x in range(0, 360)]

class Mouse(Turtle):
    """docstring for Mouse"""
    def __init__(self, position, heading, arena, fill=green, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.radius = (self.position - self.origin).length()
        self.theta = (self.m / self.radius) * 180 / pi
        self.angle = (self.position - self.origin).direction()
        self.arena = arena

    def getnextstate(self):
        """Advance around statue."""
        if self.arena.checkvar.get() == 1:
            p = (self.position - self.origin).rotate(self.theta)
        else:
            p = (self.position - self.origin).rotate(-self.theta)
        self.angle = p.direction()
        return p + self.origin, self.heading

    def donothing(self):
        """Make the turtle not move."""
        return self.position, self.heading

class Cat(Turtle):
    """docstring for Cat"""
    def __init__(self, position, heading, mouse, arena, fill=red, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.arena = arena
        self.mouse = mouse
        self.radius = (self.position - self.origin).length()
        self.theta = (self.m * 1.25 / self.radius) * 180 / pi
        self.angle = (self.position - self.origin).direction()

    def getnextstate(self):
        self.radius = (self.position - self.origin).length()
        self.theta = (self.m * 1.25 / self.radius) * 180 / pi
        if self.arena.checkvar.get() == 1:
            p = (self.position - self.origin).rotate(self.theta)
            mp = (self.mouse.position - self.origin).rotate(self.mouse.theta)
        else:
            p = (self.position - self.origin).rotate(-self.theta)
            mp = (self.mouse.position - self.origin).rotate(-self.mouse.theta)
        cat_angle = (self.position - self.origin).direction()
        mouse_angle = (self.mouse.position - self.origin).direction()
        phi = acos(self.m / self.radius).real * 180 / pi
        diff = mouse_angle - cat_angle
        if diff > 270:
            diff = 360 - diff
        if int(round(self.radius, 1)) == int(self.m):
            cat_mouse_length = sqrt(2*self.m**2 * (1 - cos((mouse_angle - cat_angle)*pi/180)))
            next_cat_mouse_length = sqrt(2*self.m**2 * (1 - cos((p.direction() - mp.direction())*pi/180)))
            #print(cat_mouse_length, next_cat_mouse_length)
            if next_cat_mouse_length > cat_mouse_length:
                self.arena.stop()
                print "Mouse caught!"
                self.getnextstate = self.donothing
                self.mouse.getnextstate = self.donothing
                mousewin = Toplevel(self.arena)
                text = Label(mousewin, text="The Cat caught the Mouse!", font='ariel 20 bold')
                text.pack()
                button = Button(mousewin, text="Ok", command=mousewin.destroy)
                button.pack()
                photo = PhotoImage(file='cat_mouse.gif')
                pic = Label(mousewin, image=photo)
                pic.photo = photo
                pic.pack()
        if abs(diff) <= phi and not self.radius <= self.m:
            u = unit((self.position - self.origin).direction())
            new_pos = (self.radius - self.m) * u
            self.radius -= self.m
            if self.radius < self.m:
                self.radius = self.m
                new_pos = self.m * u
            self.theta = (self.m * 1.25 / self.radius) * 180 / pi
            return new_pos + self.origin, self.heading
        else:
            self.angle = p.direction()
            return p + self.origin, self.heading

    def donothing(self):
        """Make the turtle not move."""
        return self.position, self.heading

def initialize():
    """Start the arena and add the statue, cat, and mouse"""
    arena = Arena(tk, 800, 600)            # Create an Arena widget, arena
    statue = Statue(Turtle.origin + Vector(0, 0),0)
    mouse = Mouse(Turtle.origin + Vector(0, -Turtle.m).rotate(40),0, arena)
    cat = Cat(Turtle.origin + Vector(0, -4*Turtle.m).rotate(100),0, mouse, arena)
    arena.pack()                           # Tell arena to pack itself on screen
    arena.add(statue)                      # Add a very simple, statue
    arena.add(mouse)                       # Add a green mouse centered at the base of the statue
    arena.add(cat)                         # Add a red cat
    arena.cat_radius.set('CatRadius: %2.f' % cat.radius)
    arena.cat_angle.set('CatAngle: %2.f' % cat.angle)
    arena.mouse_angle.set('MouseAngle: %2.f' % mouse.angle)
    arena.add_labels(arena.time, arena.cat_radius, arena.cat_angle, arena.mouse_angle)

tk = Tk()                              # Create a Tk top-level widget
initialize()
tk.mainloop()                          # Enter the Tkinter event loop
