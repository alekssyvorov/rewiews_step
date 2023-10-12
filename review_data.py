# from main import result_dict_home, result_dict_class
from data import *
from main import result_date


def writing_review(data):
    res = ""
    name, hw, cw = data[0], data[1], data[2]
    for i in data:
        if hw > 10 and cw >= 4.5:  # Сильный студент
            res = f"{name}{strong_student()}"
        if 7 < hw <= 10:
            res = f"{name}{average_student_hw()}"
        if 0 < hw <= 7:
            res = f"{name}{weak_student_hw()}"
        if 4.5 < cw < 7:
            res += f"{strong_cw()}"
        if 3 < cw < 4.5:
            res += f"{average_student_cw()}"
        if 1 < cw <= 3:
            res += f"{weak_student_cw()}"
        if 0 <= cw <= 1:
            res += f"{cw_zero()}"
        return res


# data = {1: ['Роман', 10.0, 2.4], 2: ['Дмитро', 10.0, 1.2], 3: ['Георгій', 9.17, 2.2],
#         4: ['Віталій', 9.0, 0], 5: ['Володимир', 6.33, 0], 6: ['Карина', 8.33, 3.6],
#         7: ['Іван', 11.17, 4.8], 8: ['Віктор', 10.5, 6.0], 9: ['Аліса', 11.0, 6.0],
#         10: ['Ельдар', 10.67, 4.8], 11: ['Олексій', 10.33, 4.6], 12: ['Микита', 9.67, 3.4],
#         13: ['Валерій', 10.0, 5.9], 14: ['Олександр', 5.83, 0], 15: ['Дмитро', 6.67, 4.7],
#         16: ['Станіслав', 3.5, 1.2]}
data = result_date

# for i in range(1, 17):
#     print(writing_review(data[i]))
