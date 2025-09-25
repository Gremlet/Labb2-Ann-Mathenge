import numpy as np
import math
import re
import matplotlib.pyplot as plt
import random

data_path = './data/datapoints.txt'
test_path = './data/testpoints.txt'


def read_datapoints(filepath):
    datapoints = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('('): 
                continue
            width, height, label = map(float, line.split(','))
            # convert the label value to an int because has to be 1 or 0 not 1.0 and 0.0.
            # and add width, height and label tuples to the datapoints list
            datapoints.append((width, height, int(label))) 
    return datapoints

def read_testpoints(filepath):
    testpoints = []
    list_number_pattern = re.compile(r'^\d+\.\s*') # start of line, digits, dots and whitespace
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('Test'):
                continue
            line = list_number_pattern.sub('', line) # substitute 1. 2. etc with empty string
            line = line.replace('(', '').replace(')', '')
            width, height = map(float, line.split(','))
            testpoints.append((width, height))
    return testpoints


def plot_datapoints(datapoints):
    pichus = [point for point in datapoints if point[2] == 0]
    pikachus = [point for point in datapoints if point[2] == 1]

    #split into x and y coords for pichus and pikachus
    pichu_x = [p[0] for p in pichus]
    pichu_y = [p[1] for p in pichus]

    pikachu_x = [p[0] for p in pikachus]
    pikachu_y = [p[1] for p in pikachus]

    plt.scatter(pichu_x, pichu_y, color = 'blue', label = 'Pichu')
    plt.scatter(pikachu_x, pikachu_y, color = 'yellow', label = 'Pikachu')

    plt.xlabel('Width (cm)')
    plt.ylabel('Height (cm)')
    plt.title('Pichus and Pikachus')
    plt.legend()
    plt.grid(True)
    plt.show()

# just for fun, plot the test data
# TODO: Put this in the same plot as pichus and pikachus? Could be fun to see.
def plot_testpoints(testpoints):
    x = [p[0] for p in testpoints]
    y = [p[1] for p in testpoints]

    plt.scatter(x, y, color = 'red', label = 'Test points')

    plt.title('Test data')
    plt.show()

def euclidean_distance(p1, p2):
    return math.dist(p1, p2)

def nearest_neighbour(testpoint, training_data):
    poke_data = []
    for data_point in training_data:
        coords = (data_point[0], data_point[1])
        label = 'Pikachu' if data_point[2] == 1 else 'Pichu'
        poke_data.append((euclidean_distance(testpoint, coords), label))
    neighbour = min(poke_data)
    print(f'Sample with (width, height): {testpoint} classified as {neighbour[1]}')

def classify_user_points(training_data):
    # TODO: deal with really big numbers because pokemon really shouldn't be metres long!
    while True:
        try:
            print('\nIs it a Pikachu or a Pichu? \nLet\'s classify your pokemon based on its width and height.\n')
            width = float(input('Enter the width of the pokemon in cm \n'))
            height = float(input('Enter the height of the pokemon in cm \n'))

            if width < 0 or height < 0:
                print('Width and height must be non-negative! Try again.')
                continue
            test_point = (width, height)
            nearest_neighbour(test_point, training_data)
            while True:
                try_again = input('Would you like to classify another pokemon? Y/N ').lower()
                if try_again in ('y', 'n'):
                    break
                print('Please enter Y or N (not case sensitive).')
            if try_again == 'n':
                print('Thanks for using the Pichu/Pikachu classifier!')
                break
        except ValueError:
            print('Invalid input. Please enter numerical values only.')


def classify_k_nearest_neighbours(testpoint, training_data, k=10):
    poke_data = []
    for data_point in training_data:
        coords = (data_point[0], data_point[1])
        label = data_point[2]
        poke_data.append((euclidean_distance(testpoint, coords), label))
    poke_data.sort() # sort the distances in place

    k_neighbours = poke_data[:k] # slice the first 10 values

    votes = [label for _,label in k_neighbours] # get just the labels

    prediction = 1 if votes.count(1) > votes.count(0) else 0

    # print(f'Sample with (width, height): {testpoint} classified as {'Pikachu' if prediction == 1 else 'Pichu'} ')
    return prediction

def randomly_split_data(training_data):
    pichus = []
    pikachus = []

    for point in training_data:
        if point[2] == 0:
            pichus.append(point)
        elif point[2] == 1:
            pikachus.append(point)

    random.shuffle(pichus)
    random.shuffle(pikachus)

    training_pichus = pichus[:50]
    test_pichus = pichus[50:75]

    training_pikachus = pikachus[:50]
    test_pikachus = pikachus[50:75]

    new_training_data = training_pikachus + training_pichus
    full_test_data = test_pikachus + test_pichus
    random.shuffle(full_test_data)

    test_coords = [(w, h) for (w, h, _) in full_test_data]
    test_labels = [label for (_, _, label) in full_test_data]

    random.shuffle(new_training_data)

    return new_training_data, test_coords, test_labels

def split_and_predict(training_data):
    random_training_data, test_coords, test_labels = randomly_split_data(training_data)

    tp, tn, fp, fn = 0, 0, 0, 0

    for coords, actual_label in zip(test_coords, test_labels):
        prediction = classify_k_nearest_neighbours(coords, random_training_data)
        if prediction == 1 and actual_label == 1:
            tp += 1
        elif prediction == 0 and actual_label == 0:
            tn += 1
        elif prediction == 1 and actual_label == 0:
            fp += 1
        elif prediction == 0 and actual_label == 1:
            fn += 1

    accuracy = (tp + tn) / len(test_labels)
    print(f'accuracy is {accuracy}')
    print(f'Pikachu predicted, actual Pikachu: {tp}')
    print(f'Pichu predicted, actual Pichu: {tn}')
    print(f'Pikachu predicted, actual Pichu: {fp}')
    print(f'Pichu predicted, actual Pikachu: {fn}')


    return accuracy



def main():
    training_data = read_datapoints(data_path)
    # plot_datapoints(training_data)
    testpoints = read_testpoints(test_path)
    # for point in testpoints:
    #     nearest_neighbour(point, training_data)

    # classify_user_points(training_data)

    # for point in testpoints:
    #     classify_k_nearest_neighbours(point, training_data)

    split_and_predict(training_data)



    


if __name__ == '__main__':
    main()

    
 
