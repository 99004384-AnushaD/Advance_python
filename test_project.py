from project import *

def test_list2dict():
    assert print(list2dict("{' Ps.No': 99004351, 'sem1 Marks': 78, 'sem2 Marks': 83, 'sem3 Marks': 67, 'sem4 Marks': 98, 'sem5 Marks': 70, 'sem6 Marks': 74, 'sem7 Marks': 34, 'sem8 Marks': 89, 'sem9 Marks': 94, 'sem10 Marks': 13, 'sem11 Marks': 65, 'sem12 Marks': 78, 'sem13 Marks': 33, 'sem14 Marks': 45, 'sem15 Marks': 10, 'sem16 Marks': 88, 'sem17 Marks': 4, 'sem 18 Marks': 45, 'sem 19 Marks': 33, 'Sem20 Marks': 98}")) == print(" {'Marks': {' Ps.No': 99004351, 'sem1 Marks': 78, 'sem2 Marks': 83, 'sem3 Marks': 67, 'sem4 Marks': 98, 'sem5 Marks': 70, 'sem6 Marks': 74, 'sem7 Marks': 34, 'sem8 Marks': 89, 'sem9 Marks': 94, 'sem10 Marks': 13, 'sem11 Marks': 65, 'sem12 Marks': 78, 'sem13 Marks': 33, 'sem14 Marks': 45, 'sem15 Marks': 10, 'sem16 Marks': 88, 'sem17 Marks': 4, 'sem 18 Marks': 45, 'sem 19 Marks': 33, 'Sem20 Marks': 98}}")

def test_list2dict1():
    assert print(list2dict("{' Ps.No': 99004351, 'Playing': 'Yes', 'Gardening': 'No', 'painting': 'Yes', 'shopping': 'No', 'watching movies': 'Yes', 'cooking': 'Yes', 'Drawing': 'Yes','Reading books': 'No', 'Singing': 'No', 'Dancing': 'Yes', 'House Keeping': 'No', 'Writing': 'No', 'Hiking': 'Yes', 'Travelling': 'Yes', 'Decorating': 'No', 'Exercise': 'Hiking', 'Driving': 'No', 'Swimming': 'Yes', 'Camping': 'No', 'Music': 'Yes'}")) == print("{'Hobbies': {' Ps.No': 99004351, 'Playing': 'Yes', 'Gardening': 'No', 'painting': 'Yes', 'shopping': 'No', 'watching movies': 'Yes', 'cooking': 'Yes', 'Drawing': 'Yes', 'Reading books': 'No', 'Singing': 'No', 'Dancing': 'Yes', 'House Keeping': 'No', 'Writing': 'No', 'Hiking': 'Yes', 'Travelling': 'Yes', 'Decorating': 'No', 'Exercise': 'Hiking', 'Driving': 'No', 'Swimming': 'Yes', 'Camping': 'No', 'Music': 'Yes'}}")

def test_list2dict2():
    assert print(list2dict("{' Ps.No': 99004357, 'Wireless communication': 4, 'IoT': 4, 'AI': 2, 'Cyber Security': 3, 'Vlsi': 0, 'Cloud Computing': 3, 'Data Science': 4, 'Computer Vision': 4, 'Machine Learning': 4, 'Big Data': 3, 'Data Mining': 4, 'Data Analytics': 2, 'Robotics': 3, 'Edge Computing': 2, 'Block Chain': 0, 'Database': 1, 'Algorithms': 0, 'Cryptography': 1, '5G': 0, 'RPA': 2}")) == print("{'Domain': {' Ps.No': 99004357, 'Wireless communication': 4, 'IoT': 4, 'AI': 2, 'Cyber Security': 3, 'Vlsi': 0, 'Cloud Computing': 3, 'Data Science': 4, 'Computer Vision': 4, 'Machine Learning': 4, 'Big Data': 3, 'Data Mining': 4, 'Data Analytics': 2, 'Robotics': 3, 'Edge Computing': 2, 'Block Chain': 0, 'Database': 1, 'Algorithms': 0, 'Cryptography': 1, '5G': 0, 'RPA': 2}}")

def test_data():
    assert print(load_excel("C:\\Users\\AAA\\OneDrive\\Desktop\\python-data.xlsx") ) == print("<openpyxl.workbook.workbook.Workbook object at 0x000001ADA8163400>\n<openpyxl.workbook.workbook.Workbook object at 0x000001ADA81633A0>")