import joblib
import random
from catboost import CatBoost


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
    model = CatBoost.load_model('C:/Users/sycwd/Desktop/NTU/save_model/heart_family_clf.pkl')
    return model


def load_heart_professional():
    model = CatBoost.load_model('C:/Users/sycwd/Desktop/NTU/save_model/heart_professional_clf.pkl')
    return model


def pred_value_simulation(pred):
    simulated_term = random.uniform(0.7,1)
    return pred * simulated_term if pred else pred + 1 - simulated_term


def get_result(version, disease, data):
    if version == 'Premiere':
        model = eval(professionalDict[disease])
    elif version == 'Community':
        model = eval(familyDict[disease])
    elif version == 'Special':
        model = load_mental()
    pred_value = pred_value_simulation(model.predict(data))
    return pred_value

