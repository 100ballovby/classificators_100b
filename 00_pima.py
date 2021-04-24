import csv
import math
import random


def load_data(lines):
    readed = csv.reader(open(lines))
    dataset = list(readed)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def spit_data(dataset, ratio):
    trainSize = int(len(dataset) * ratio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

def sep_by_class(dataset):
    separated_data = {}
    for item in range(len(dataset)):
        v = dataset[item]
        if v[-1] not in separated_data:
            separated_data[v[-1]] = []
            separated_data[v[-1]].append(v)
    return separated_data

def mean(numbers):
    return sum(numbers) / len(numbers)

def difference(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)

def sum_dataset(dataset):
    sum = [(mean(attr), difference(attr)) for attr in zip(*dataset)]
    del sum[-1]
    return sum

def sum_classes(dataset):
    separated = sep_by_class(dataset)
    summary = {}
    for value, instance in separated.items():
        summary[value] = sum_dataset(instance)
    return summary

## шаг 3. Предсказания.
def calc_probability(x, mean, diff):
    exp = math.exp(
        -( math.pow(x - mean, 2) / (2 * math.pow(diff, 2)) )
    )
    res = (1 / (math.sqrt(2 * math.pi) * diff)) * exp
    return res

def calc_class_probabilities(summaries, inputV):
    prob = {}
    for classValue, classSummaries in summaries.items():
        prob[classValue] = 1
        for i in range(len(classSummaries)):
            mean, diff = classSummaries[i]
            x = inputV[i]
            prob[classValue] *= calc_probability(x, mean, diff)
    return prob

def predict(summaries, inputV):
    prob = calc_class_probabilities(summaries, inputV)
    bestLabel = None
    bestProb = -1
    for classValue, probability in prob.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel

def get_prediction(summaries, test_data):
    predictions = []
    for i in range(len(test_data)):
        res = predict(summaries, test_data[i])
        predictions.append(res)
    return predictions

def get_accuracy(test_data, predictions):
    correct = 0
    for i in range(len(test_data)):
        if test_data[i][-1] == predictions[i]:
            correct += 1
    return (correct / len(test_data)) * 100.0

def main():
    filename = 'pima-indians-diabetes.csv'
    dataset = load_data(filename)
    ratio = 0.57
    train_data, test_data = spit_data(dataset, ratio)
    print(f'''Разделено {len(dataset)} строк? на:
    1. Тренировочные данные: {len(train_data)}
    2. Тестовое данные: {len(test_data)}''')
    summaries = sum_classes(train_data)
    print(summaries)

    #prediction = get_prediction(summaries, test_data)

    #accuracy = get_accuracy(test_data, prediction)
    #print(f'Точность: {accuracy}')


if __name__ == '__main__':
    main()

