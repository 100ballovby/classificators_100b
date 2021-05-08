from dicerolling import Dice
import thinkplot  # использует matplotlib и рисует графики, основываясь на байесе


class Train(Dice):
    '''Основан на классе из задачи про кубики. Работает так же.
    Логика работы Likelihood такая же, как у Dice
    '''

hypos = range(1, 1001)  # 1/N
s = Train(hypos)
s.Update(60)

print(s.Mean())
thinkplot.PrePlot(1)
thinkplot.Pmf(s)
thinkplot.Save(root='train1',
               xlabel='Количество поездов',
               ylabel='Вероятность',
               formats=['pdf', 'eps', 'jpg'])
