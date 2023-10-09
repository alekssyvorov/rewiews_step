# def sum_numbers(text: str) -> int:
#     result = []
#     summa = 0
#     for i in text.split(): # This picture is -> ["This", "picture", "is"]
#         if i.isdigit():
#             result.append(i)
#     for i in result:
#         summa = summa + int(i)
#     return summa
def sum_numbers(text: str) -> int:
    return sum(list(map(int, [i for i in text.split() if i.isdigit()])))
print(sum_numbers("This picture is an oil on canvas painting by "
        "Danish artist Anna Petersen between 1845 and 1910 year"))