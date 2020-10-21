# -*- coding: utf-8 -*-

questiondictMapping = {
    "FP": "fluPreDict",
    "FC": "fluComDict",
    "MS": "mentalDict",
    "HP": "heartPreDict",
    "HC": "heartComDict"
}


fluPreDict = {
    "Is your temperature over 37.3℃?": ["No", "Yes"],
    "Do you feel tired?": ["No", "Yes"],
    "Do you have dry cough?": ["No", "Yes"],
    "Do you have difficulty in breathing?": ["No", "Yes"],
    "Do you have sore throat?": ["No", "Yes"],
    "Do you feel any pain?": ["No", "Yes"],
    "Do you have nasal congestion?": ["No", "Yes"],
    "Do you have runny nose?": ["No", "Yes"],
    "Do you have diarrhea?": ["No", "Yes"],
    "What is your gender? ": ["Female", "Male"],
    "Have you been in contact with anyone with the flu": ["No", "Yes"],
    "Does the patient have an antibody of flu?": ["No", "Yes"],
    "Does the patient have chronic medical conditions?": ["No", "Yes"],
    "Does the patient have seizures?": ["No", "Yes"],
    "Does the patient feel an increase in urination?": ["No", "Yes"]
}


fluComDict = {
    "Is your temperature over 37.3℃?":["No", "Yes"],
    "Do you feel tired?":["No", "Yes"],
    "Do you have dry cough?":["No", "Yes"],
    "Do you have difficulty in breathing?":["No", "Yes"],
    "Do you have sore throat?":["No", "Yes"],
    "Do you feel any pain?":["No", "Yes"],
    "Do you have nasal congestion?":["No", "Yes"],
    "Do you have runny nose?":["No", "Yes"],
    "Do you have diarrhea?":["No", "Yes"],
    "What is your gender? ":["Female", "Male"],
    "Have you been in contact with anyone with the flu":["No", "Yes"]
}


mentalDict = {
    "How old are you?": "",
    "What is your gender?":["Female", "Male"],
    "If you have a mental health condition, you feel that it interferes with your work?": ["Don't know", "Never",
                                                                                           "Often", "Rarely",
                                                                                           "Sometimes"],
    "Do you have a family history of mental illness?":["No", "Yes"],
    "Do you know the options for mental health care your employer provides?":["No", "Not sure", "Yes"],
    "Does your employer provide mental health benefits?": ["Don't know", "No", "Yes"],
    "Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment?":[
        "Don't know", "No", "Yes"],
    "How easy is it for you to take medical leave for a mental health condition?":["Don't know", "Somewhat difficult",
                                                                                    "Somewhat easy", "Very difficult",
                                                                                    "Very easy"],
    "Have you heard of or observed negative consequences for coworkers with mental health conditions in your company?":[
        "No", "Yes"
    ],
    "Would you bring up a mental health issue with a potential employer in an interview?":["Maybe", "No", "Yes"],
    "Has your employer ever discussed mental health as part of an employee wellness program?":["Don't know", "No", "Yes"],
    "Does your employer provide resources to learn more about mental health issues and how to seek help?":["Don't know", "No", "Yes"]
}


heartPreDict = {
    "How old is the patient?":"",
    "What is the gender of the patient?": ["Female", "Male"],
    "What is the chest pain type of the patient?": ["continuous angina", "discontinuous angina", "non-anginal pain",
                                                   "asymptomatic"],
    "What is the resting blood pressure of the patient?": "",
    "What is the serum cholesterol of the patient (in mg/dl)?":"",
    "Is the patient’s fasting blood sugar higher than 120mg/dl?":["No", "Yes"],
    "What is the resting electrocardiographic result of the patient?":["normal", "having ST-T wave abnormality",
                                                                       "definite left ventricular hypertrophy"],
    "What is the patient's maximum heart rate achieved?":"",
    "Does the patient have exercise induced angina?":["No", "Yes"],
    "Does the patient have ST depression induced by exercise relative to rest?":["No", "Yes"],
    "What is the patient’s slope of the peak exercise ST segment (an integer from 0 to 2)?":"",
    "How many major vessels of the patient are colored by fluoroscopy (maximum 3)":"",
    "Does the patient have any heart defect previously?":["no","fixed defect", "reversable defect"]
}


heartComDict = {
    "How old are you?":"",
    "What's your gender?": ["Female", "Male"],
    "What kind of chest pain type do you have?":["continuous angina", "discontinuous angina", "non-anginal pain",
                                                   "asymptomatic"],
    "What is your resting blood pressure?":"",
    "What is your maximum heart rate achieved recently?":"",
    "Do you have exercise induced angina?":["No", "Yes"],
    "Do you have any heart defect previously?":["no","fixed defect", "reversable defect"]
}