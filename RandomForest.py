from sklearn.ensemble import RandomForestClassifier
import numpy as np
import random


def get_train_test_data(in_data, records_count):
    random.shuffle(in_data)
    test_data = in_data[:records_count]
    train_data = in_data[records_count+1:]
    return train_data, test_data


if __name__ == "__main__":
    rf = RandomForestClassifier(n_jobs=2)
    inp_file = raw_input("Enter the input file path: ")
    in_data = np.loadtxt(inp_file, dtype=int, delimiter=',')
    for i in range(0,5):
        print("Test Sample: " + str(i))
        records_count = 100
        train_data, test_data = get_train_test_data(in_data, records_count)
        target = train_data[:,-1]
        train = train_data[:,[x for x in range(0,22)]]
        rf.fit(train, target)
        test = test_data[:,[x for x in range(0,22)]]
        result = rf.predict(test)
        correct = 0
        for i in range(0,records_count):
            if test_data[i][22] == result[i]:
                correct += 1
        print("Accuracy:")
        print(float(correct)/records_count)*100
        print("___________________")