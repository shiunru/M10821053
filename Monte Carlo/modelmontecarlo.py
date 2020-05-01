import model

flog = True

while flog:
    type_select = eval(input('ccp test'))

    if type_select == 1:
        model.normal_type()
        continue
    elif type_select == 2:
        model.upward_trend_type()
        continue
    elif type_select == 3:
        model.downward_trend_type()
        continue
    elif type_select == 4:
        model.upward_shift_type()
        continue
    elif type_select == 5:
        model.downward_shift_type()
        continue
    elif type_select == 6:
        model.cycle_type()
        continue
    elif type_select == 7:
        model.systematic_type()
        continue
    elif type_select == 8:
        model.stratification_type()
        continue
    elif type_select == 0:
        flog = False
        break
    else:
        print('error')
        continue
