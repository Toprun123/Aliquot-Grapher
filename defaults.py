import cairo, sys, gi
from multiprocessing import Process, Lock
gi.require_version("Gtk", "4.0")
gi.require_version("GLib", "2.0")
from gi.repository import GLib, Gtk, Gio, Gdk

WINDOW_DEF_HEIGHT = 600
WINDOW_DEF_WIDTH = 750

def sum_fact(x):
    r = 0
    for i in range(1, x):
       if x % i == 0:
           r+=i
    return r

def aliquot(x):
    r = []
    for _ in range(250):
        if x == 0:
            return r
        else:
            x = sum_fact(x)
            r.append(x)
    return r

def on_draw(da, ctx, w, h, seq):
    x, y = 0, h
    ctx.set_line_width (6)
    ctx.move_to(-w, h)
    i = (h/max(seq))*0.9
    t = len(seq)
    j = (w/t)*0.8
    if j>37:
        j = 37
    elif j<30:
        j = 30
    for e in seq:
        y=h+(-e*i)
        ctx.line_to(x, y)
        x+=j
    ctx.stroke()

# 14316, 220, 30, 180, 2018, 1000140

