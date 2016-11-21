import pandas as pd
import random
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def get_train_test_data(in_data, records_count):
    random.shuffle(in_data)
    test_data = in_data[:records_count]
    train_data = in_data[records_count+1:]
    return train_data, test_data


def generate_model():
    data_file = pd.read_csv("D:\\Education\\ASU\SML\\Project\\Expedia\\TrainData\\sample.csv")
    print data_file.columns
    model = pd.DataFrame()
    model['user_country'] = data_file['user_location_country']
    model['user_region'] = data_file['user_location_region']
    model['user_city'] = data_file['user_location_city']
    model['userid'] = data_file['user_id']
    model['ispackage'] = data_file['is_package']
    model['srchci'] = data_file['srch_ci']
    model['srchco'] = data_file['srch_co']
    model['srchadults_cnt'] = data_file['srch_adults_cnt']
    model['srchchildren_cnt'] = data_file['srch_children_cnt']
    model['srchrm_cnt'] = data_file['srch_rm_cnt']
    model['srchdestination_id'] = data_file['srch_destination_id']
    model['srchdestination_type_id'] = data_file['srch_destination_type_id']
    model['isbooking'] = data_file['is_booking']
    model['hotelcountry'] = data_file['hotel_country']
    model['hotelmarket'] = data_file['hotel_market']
    model['hotelcluster'] = data_file['hotel_cluster']
    y = model['hotelcluster']
    model = model.drop(['hotelcluster'], axis=1)
    print "model classification done"
    scaler = StandardScaler()
    model = scaler.fit_transform(model)
    model_train, model_test, cluster_train, cluster_test = train_test_split(model, y, test_size=0.2, random_state=42)
    logit_model = LogisticRegression(penalty='l2')
    logit_model.fit(model_train, cluster_train)
    print logit_model.predict(model_test)
    print "Logistic regression is %2.2f" % accuracy_score(cluster_test, logit_model.predict(model_test))


generate_model()