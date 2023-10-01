"""
Random walk traditional
"""
import collections

size(640, 240)
speed(30)
walker = None

def constrain(v, min, max):
  if v < min:
    return min
  elif v > max:
    return max
  else:
    return v

class Walker:
  def __init__(self):
    self.x = WIDTH // 2
    self.y = HEIGHT // 2
    self.q = collections.deque()

  def show(self):
      stroke(0.8)
      for (x, y) in self.q:
          rect(x, y, 1, 1)

      stroke(0)
      rect(self.x, self.y, 1, 1)
      self.q.append((self.x, self.y))
      if len(self.q) > 500:
          self.q.popleft()

  def step(self):
    choice = random(4)
    if choice == 0:
      self.x += 1
    elif choice == 1:
      self.x -= 1
    elif choice == 2:
      self.y += 1
    else:
      self.y -= 1

    self.x = constrain(self.x, 0, WIDTH)
    self.y = constrain(self.y, 0, HEIGHT)


def setup():
    global walker
    walker = Walker()
    background(1.0)

def draw():
    walker.step()
    walker.show()