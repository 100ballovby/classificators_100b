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
            return 1.0/hypo