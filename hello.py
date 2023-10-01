"""
Hello world
"""
size(640, 240)
speed(60)

x = 0
y = 50
txt = '你好世界'
w, _h = textmetrics(txt)

def setup():
    background(255, 255, 255)

def draw():
    global x, y
    fill(0)
    text(txt, x, y)
    if x+w > WIDTH:
        x = 0
        y += 50
    else:
        x += 1
