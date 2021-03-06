from sklearn.ensemble import RandomForestClassifier
import numpy as np
import random


def get_train_test_data(in_data, records_count):
    random.shuffle(in_data)
    test_data = in_data[:records_count]
    train_data = in_data[records_count+1:]
    return train_data, test_data


if __name__ == "__main__":
    inp_file = raw_input("Enter the input file path: ")
    in_data = np.loadtxt(inp_file, dtype=int, delimiter=',')
    for i in range(0,5):
        rf = RandomForestClassifier(n_jobs=2)
        print("Test Sample: " + str(i))
        records_count = 100
        train_data, test_data = get_train_test_data(in_data, records_count)
        target = train_data[:,-1]
        train = train_data[:,[x for x in range(0,22)]]
        rf.fit(train, target)
        test = test_data[:,[x for x in range(0,22)]]
        test_result = test_data[:,-1]
        accuracy = rf.score(test, test_result)
        print("Accuracy:")
        print(accuracy)
        print("___________________")
