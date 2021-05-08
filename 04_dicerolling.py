from thinkbayes2 import Suite


class Dice(Suite):
    def Likelihood(self, data, hypo):
        """Считает вероятность данных по гипотезе
        hypo: число граней на игральной кости
        data: число бросков кубика
        """
        if hypo < data:
            return 0
        else:
            return 1.0 / hypo

s = Dice([4, 6, 8, 12, 20])
s.Update(6)  # если подбросили кубик и получили 6
print('После подбрасывания куба и выпадения 6')
s.Print()

for roll in [6, 5, 7, 6, 7, 3]:
    s.Update(roll)

print('\n\nПосле нескольких подбрасываний')
s.Print()