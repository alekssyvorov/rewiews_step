
def result(hw: dict, cw: dict, count_hw: int, count_cw: int) -> dict:
    res = {}
    lst_hw = []
    lst_cw = []
    for i in list(hw):
        lst_hw.append(i[i.find(" ")+1:i.rfind(" ")])
    for i in list(cw):
        lst_cw.append(i[i.find(" ")+1:i.rfind(" ")])

    for i in range(len(hw)):
        temp_hw = (list(hw.values()))[i]
        temp_cw = (list(cw.values()))[i]
        if len(temp_hw) > 0 and len(temp_cw) != 0:
            res[i+1] = [lst_hw[i], round(sum(map(int, temp_hw))/count_hw, 2), round(sum(map(int, temp_cw))/count_cw, 2)]
        elif len(temp_hw) > 0 and len(temp_cw) == 0:
            res[i+1] = [lst_hw[i], round(sum(map(int, temp_hw))/count_hw, 2), 0]
        elif len(temp_hw) == 0 and len(temp_cw) > 0:
            res[i+1] = [lst_hw[i], 0, round(sum(map(int, temp_cw))/count_cw, 2)]
        elif len(temp_hw) == 0 and len(temp_cw) == 0:
            res[i+1] = [lst_hw[i], 0, 0]
    return res