import os
import pandas as pd
import json

def convert_five_option_question(answer, is_score_direction_good = False):
    # if score direction is good, bigger score means better condition (smaller problem)
    is_score_direction_good = False
    if answer == 1:
        return "0" if is_score_direction_good else "100"
    elif answer == 2:
        return "25" if is_score_direction_good else "75"
    elif answer == 3:
        return "50"
    elif answer == 4:
        return "75" if is_score_direction_good else "25"
    elif answer == 5:
        return "100" if is_score_direction_good else "0"
    else: # default if NULL or invalid value
        return "0" if is_score_direction_good else "100"

def convert_four_option_question(answer, is_score_direction_good = True):
    # if score direction is good, bigger score means better condition (smaller problem)
    is_score_direction_good = False
    if answer == 1:
        return "0" if is_score_direction_good else "100"
    elif answer == 2:
        return "33" if is_score_direction_good else "67"
    elif answer == 3:
        return "67" if is_score_direction_good else "33"
    elif answer == 4:
        return "100" if is_score_direction_good else "0"
    else: # default if NULL or invalid value
        return "0" if is_score_direction_good else "100"

# Read data input
excel_data_df = pd.read_excel('PROM-RulesBasedAlgorithmData_R2.0.xlsx', sheet_name='PROM-RulesBasedAlgorithmData_R2')
output_dir = "./input_data_au"

# Clear previous runtime results
os.system(f'rm -rf {output_dir}')
os.mkdir(output_dir)

for i in range(len(excel_data_df)):
    patient_id = excel_data_df.loc[i, "CapstudiesID"]
    survey_id = excel_data_df.loc[i, "PROAnswerSetID"]
    patient_dir = f"{output_dir}/{patient_id}"
    if not os.path.isdir(patient_dir): # make sure each patient has their own folder
        os.mkdir(patient_dir)
  
    survey_data = {"resource": 
        {
            "authored" : str(excel_data_df.loc[i, "AproxPromDate"]),
            "item" : [
                {
                    "linkId": "Urinary Incontinence",
                    "item": [
                        {
                            "linkId": "UI_1",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode1"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "UI_2",
                            "answer": [
                                {
                                    "valueString": convert_four_option_question(excel_data_df.loc[i, "QueEpicAnsCode2"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "UI_3",
                            "answer": [
                                {
                                    "valueString": convert_four_option_question(excel_data_df.loc[i, "QueEpicAnsCode3"], is_score_direction_good=True)
                                }
                            ]
                        },
                        {
                            "linkId": "UI_4",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode4A"], is_score_direction_good=False)
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "Urinary Obstructive",
                    "item": [
                        {
                            "linkId": "UO_5",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode4B"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "UO_6",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode4C"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "UO_7",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode4D"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "UO_8",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode4E"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "UO_9",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode5"], is_score_direction_good=False)
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "Bowel Function",
                    "item": [
                        {
                            "linkId": "B_10",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode6A"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "B_11",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode6B"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "B_12",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode6C"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "B_13",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode6D"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "B_14",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode6E"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "B_15",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode7"], is_score_direction_good=False)
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "Sexual Function",
                    "item": [
                        {
                            "linkId": "S_16",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode8A"], is_score_direction_good=True)
                                }
                            ]
                        },
                        {
                            "linkId": "S_17",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode8B"], is_score_direction_good=True)
                                }
                            ]
                        },
                        {
                            "linkId": "S_18",
                            "answer": [
                                {
                                    "valueString": convert_four_option_question(excel_data_df.loc[i, "QueEpicAnsCode9"], is_score_direction_good=True)
                                }
                            ]
                        },
                        {
                            "linkId": "S_19",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode10"], is_score_direction_good=True)
                                }
                            ]
                        },
                        {
                            "linkId": "S_20",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode11"], is_score_direction_good=True)
                                }
                            ]
                        },
                        {
                            "linkId": "S_21",
                            "answer": [
                                {
                                    "valueString": convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode12"], is_score_direction_good=False)
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "Hormonal State",
                    "item": [
                        {
                            "linkId": "H_22",
                            "answer": [
                                {
                                    "valueString":  convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode13A"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "H_23",
                            "answer": [
                                {
                                    "valueString":  convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode13B"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "H_24",
                            "answer": [
                                {
                                    "valueString":  convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode13C"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "H_25",
                            "answer": [
                                {
                                    "valueString":  convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode13D"], is_score_direction_good=False)
                                }
                            ]
                        },
                        {
                            "linkId": "H_26",
                            "answer": [
                                {
                                    "valueString":  convert_five_option_question(excel_data_df.loc[i, "QueEpicAnsCode13E"], is_score_direction_good=False)
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }

    survey_json = excel_data_df.loc[i].to_json()
    json_path = f'{patient_dir}/{patient_id}_{survey_id}.json'
    
    with open(json_path, 'w') as f: # create a json file for each survey
        json.dump(survey_data, f, indent=4)

