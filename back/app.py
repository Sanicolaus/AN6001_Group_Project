from flask import Flask
from flask_cors import *
from chatbot_interface import get_result
import question_dict
import numpy as np

app = Flask(__name__)
CORS(app, supports_credentials=True)


# Mark the position of current question in the question dictionary
glVar = None
# Record the length of question dictionary
varRange = None
# Record current disease
disease = None
# Record current version
version = None
# Referred as current question dictiionary
questionDict = None
# Record user's information
data = None
# Triage priority recording
priority = {
    "Flu":[],
    "Heart Disease":[]
}
versionList = ['Premium', 'Community', 'Special']
diseaseList = ['Flu', 'Heart Disease', 'Mental Depression']


# Initiate global variables
def initGlvar():
    global glVar, varRange, disease, versionList,data, questionDict
    index = disease[0] + version[0]
    questionDict = getattr(question_dict, question_dict.questiondictMapping[index])
    glVar = 0
    varRange = len(questionDict)
    data = []


# Reset global variables
def resetGlvar():
    global glVar, varRange, disease, version, questionDict
    glVar = None
    varRange = None
    disease = None
    version = None
    questionDict = None

# Used as a test interface. Nothing to do normally
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/asked/<string:question>')
def answer(question):
    global version, versionList, disease, glVar, varRange, questionDict, data
    # Receive the version parameter from user.
    if question in versionList:
        version = question
        return {'questions': 'Thank you. Please enter the name of targeted disease.',
                'suggestions': diseaseList}
    # Firstly check whether there is a valid version
    if version is None:
        return {'questions': 'Please select the version of triage chatbot.',
                'suggestions': versionList}
    # Receive the disease parameter from user.
    if question in diseaseList:
        disease = question
        initGlvar()
        print(questionDict)
        glVar += 1
        # Post the first question in question dictionary
        if list(questionDict.values())[glVar-1] != "":
            return {'questions': list(questionDict.keys())[glVar-1],
                    'suggestions': list(questionDict.values())[glVar-1]}
        else:
            return {'questions': list(questionDict.keys())[glVar - 1]}
    # Receive answers from user with each question. Record those information in global variable data
    if glVar <= varRange - 1:
        if list(questionDict.values())[glVar - 1] != "":
            # label encoding
            data.append(list(questionDict.values())[glVar - 1].index(question))
        else:
            data.append(eval(question))
        glVar += 1
        # Post the next question
        if list(questionDict.values())[glVar - 1] != "":
            return {'questions': list(questionDict.keys())[glVar - 1],
                    'suggestions': list(questionDict.values())[glVar - 1]}
        else:
            return {'questions': list(questionDict.keys())[glVar - 1]}
    # After receiving all questions, post a predicted value.
    elif glVar == varRange:
        if list(questionDict.values())[glVar - 1] != "":
            data.append(
                list(questionDict.values())[glVar - 1].index(question))
        else:
            data.append(eval(question))
        data = np.asarray(data).reshape(1,-1)
        # predValue = get_result(version, disease,data)
        predValue = 0.98
        if version == 'Premium':
            priority[disease].append(predValue)
            message = f"The probability is {predValue*100:.2f}%. There are {sorted(priority[disease], reverse=True).index(predValue)} patients waiting before your patient."
        else:
            message = f"The probability is {predValue*100:.2f}%, bye."
        resetGlvar()
        return {'questions': message}