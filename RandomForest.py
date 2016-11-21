from sklearn.ensemble import RandomForestClassifier
import numpy as np
import random


if __name__ == "__main__":
    rf = RandomForestClassifier(n_jobs=2)
    inp_file = raw_input("Enter the input file path: ")
    in_data = np.loadtxt(inp_file, dtype=int, delimiter=',')
    target = in_data[:,-1]
    train = in_data[:,[x for x in range(0,22)]]
    rf.fit(train, target)
    len = 1000
    test_data = np.asarray(random.sample(in_data,len))
    test = test_data[:,[x for x in range(0,22)]]
    result = rf.predict(test)
    correct = 0
    for i in range(0,len):
        if test_data[i][22] == result[i]:
            correct += 1

    print(float(correct)/len)*100