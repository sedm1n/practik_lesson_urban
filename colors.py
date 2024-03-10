class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode
        # self._hexcode = None

    @property
    def hexcode(self):
        return self._hexcode
    @hexcode.setter
    def hexcode(self, hc):
        self.r = int(hc[:2], 16)
        self.g = int(hc[2:4], 16)
        self.b = int(hc[4:], 16)
        self._hexcode = hc



col = Color('FF00FF')
print(col.r)
print(col.g)
print(col.b)
print(col.hexcode)
col.hexcode = 'FFFFFF'
print(col.hexcode)