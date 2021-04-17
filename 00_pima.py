import csv
import math
import random


def load_data():
    lines = 'pima-indians-diabetes.csv'
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
    return sum(numbers) / float(len(numbers))


def difference(numbers):
    avg = mean(numbers)
    print(avg)
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
