class Box:
    def __init__(self, inhalt):
        self.inhalt = inhalt


box2 = Box("Hallo Welt!")
box1 = Box(box2)

box3 = Box(box2)


box_wtf = Box(None)
box_wtf.inhalt = box_wtf

print(box_wtf)
print(box_wtf.inhalt.inhalt.inhalt.inhalt)
