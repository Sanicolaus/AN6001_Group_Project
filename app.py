from flask import Flask
from flask_cors import *
from chatbot_interface import get_result
import question_dict
import numpy as np

app = Flask(__name__)
CORS(app, supports_credentials=True)


glVar = None
varRange = None
disease = None
version = None
questionDict = None
data = None
versionList = ['Premiere', 'Community', 'Special']
diseaseList = ['Flu', 'Heart Disease', 'Mental Depression']


def initGlvar():
    global glVar, varRange, disease, versionList,data, questionDict
    index = disease[0] + version[0]
    questionDict = getattr(question_dict, question_dict.questiondictMapping[index])
    glVar = 0
    varRange = len(questionDict)
    data = []


def resetGlvar():
    global glVar, varRange, disease, version, questionDict
    glVar = None
    varRange = None
    disease = None
    version = None
    questionDict = None


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/asked/<string:question>')
def answer(question):
    global version, versionList, disease, glVar, varRange, questionDict, data
    if question in versionList:
        version = question
        return 'Thank you. Please enter the name of targeted disease.'
    if version is None:
        return 'Please select the version of triage chatbot.'
    if question in diseaseList:
        disease = question
        initGlvar()
        print(questionDict)
        glVar += 1
        if list(questionDict.values())[glVar-1] != "":
            return {'questions': list(questionDict.keys())[glVar-1],
                    'suggestions': list(questionDict.values())[glVar-1]}
        else:
            return {'questions': list(questionDict.keys())[glVar - 1]}
    if glVar <= varRange - 1:
        if list(questionDict.values())[glVar - 1] != "":
            data.append(list(questionDict.values())[glVar - 1].index(question))
        else:
            data.append(eval(question))
        glVar += 1
        if list(questionDict.values())[glVar - 1] != "":
            return {'questions': list(questionDict.keys())[glVar - 1],
                    'suggestions': list(questionDict.values())[glVar - 1]}
        else:
            return {'questions': list(questionDict.keys())[glVar - 1]}
    elif glVar == varRange:
        if list(questionDict.values())[glVar - 1] != "":
            data.append(
                list(questionDict.values())[glVar - 1].index(question))
        else:
            data.append(eval(question))
        data = np.asarray(data).reshape(1,-1)
        print(data)
        predValue = get_result(version, disease,data)
        resetGlvar()
        return f"The probability is {predValue}, bye."
