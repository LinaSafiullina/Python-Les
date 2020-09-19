class Table:
    def __init__(self, l, w, h):
        self.lenght = l
        self.width = w
        self.height = h

class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p

class DeskTable(Table):
    def square(self):
        return self.width*self.lenght

class ComputerTable(DeskTable):
    def square(self,e):
        return DeskTable.square - e
