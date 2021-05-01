from thinkbayes2 import Pmf
# probability mass function
# вероятностная функция масс


class Bulochki(Pmf):
    def __init__(self, h):
        Pmf.__init__(self)
        for x in h:
            self.Set(x, 1)
        self.Normalize()

    def update(self, data):
        for x in self.Values():
            like = self.Likelihood(data)
            self.Normalize(x, like)
        self.Normalize()

    mix = {
        'Bulka 1': dict(vanilla=0.75, choco=0.25),
        'Bulka 2': dict(vanilla=0.5, choco=0.5)
    }

    def Likelihood(self, data, x):
        mix = self.mix[x]
        like = mix[data]
        return like


my_list = ['Bulka 1', 'Bulka 2']
pmf = Bulochki(my_list)
pmf.update('vanilla')

for k, v in pmf.Items():
    print(k, v)