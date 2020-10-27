import joblib
import random
from catboost import CatBoostClassifier


professionalDict = {
    'Flu':'load_flu_professional()',
    'Heart Disease':'load_heart_professional()'
}

familyDict = {
    'Flu':'load_flu_family()',
    'Heart Disease':'load_heart_family()'
}


def load_mental():
    model = joblib.load('C:/Users/sycwd/Desktop/NTU/save_model/mental_model.pkl')
    return model


def load_flu_family():
    model = joblib.load('C:/Users/sycwd/Desktop/NTU/save_model/flu_community.pkl')
    return model


def load_flu_professional():
    model = joblib.load('C:/Users/sycwd/Desktop/NTU/save_model/flu_professional.pkl')
    return model


def load_heart_family():
    model = CatBoostClassifier()
    model.load_model('C:/Users/sycwd/Desktop/NTU/save_model/heart_family_clf')
    return model


def load_heart_professional():
    model = CatBoostClassifier()
    model.load_model('C:/Users/sycwd/Desktop/NTU/save_model/heart_professional_clf')
    return model


#def pred_value_simulation(pred):
#    simulated_term = random.uniform(0.7,1)
#    return pred * simulated_term if pred else pred + 1 - simulated_term


# Special data encoding for heart disease
def tach_transform(value):
    if value == 0:
        return 3
    elif value == 1:
        return 6
    elif value == 2:
        return 7


# Get the predicted value for one record.
def get_result(version, disease, data):
    if version == 'Premiere':
        model = eval(professionalDict[disease])
        if disease == 'Heart Disease':
            data[0][2] += 1
            data[0][12] = tach_transform(data[0][12])
    elif version == 'Community':
        model = eval(familyDict[disease])
        if disease == 'Heart Disease':
            data[0][2] += 1
            data[0][6] = tach_transform(data[0][6])
    elif version == 'Special':
        model = load_mental()
        data[0][0] = (data[0][0] - 5)/67
    pred_value = model.predict_proba(data)[0][1]
    return pred_value

