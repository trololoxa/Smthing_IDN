class Idn:
    def __init__(self, n, c=0):
        self.n = n
        self.c = c

    def ch(self, c):
        self.c = c

    def prnt(self):
        print('id =', id(self))
        print('c id =', id(self.c))
        print('n id =', id(self.n))
        print()
        print('c =', self.c)
        print('n =', self.n)
        print('\n')


a = Idn(1, 2)
b=a
a.prnt()
b.prnt()
b.ch(5)
b.prnt()

