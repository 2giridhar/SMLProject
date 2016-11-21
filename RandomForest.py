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
    test_data = random.sample(in_data,10)
    test = test_data[:,[x for x in range(0,22)]]
    print rf.predict(test)