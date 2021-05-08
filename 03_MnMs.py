from thinkbayes2 import Suite


class M_and_Ms(Suite):
    mix94 = dict(
        blue=0,
        brown=30,
        yellow=20,
        red=20,
        green=10,
        orange=10,
        yebrown=10,
    )
    mix96 = dict(
        blue=24,
        brown=13,
        yellow=14,
        red=13,
        green=10,
        orange=16,
        yebrown=0
    )
    hA = dict(bag1=mix94, bag2=mix96)
    hB = dict(bag1=mix96, bag2=mix94)

    hypothesis = dict(A=hA, B=hB)

    def Likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypothesis[hypo][bag]
        like = mix[color]
        return like


s = M_and_Ms('AB')
s.Update(('bag1', 'yellow'))
s.Update(('bag2', 'green'))
s.Print()
