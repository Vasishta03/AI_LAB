import random

def F(x):
    return 4*x + 10 - (x**2)

Range_min = -10
Range_max = 10
step_val = 0.1

Range = list(range(Range_min,Range_max,1))
Cur_Val = Range[int(random.random()*len(Range))]

while True:
    if Cur_Val < Range_min or Cur_Val > Range_max:
        print("Search value out of range")
        break

    neighb_1,neighb_2 = Cur_Val - step_val,Cur_Val + step_val
    f_Cur_Val,f_neighb_1,f_neighb_2 = F(Cur_Val),F(neighb_1),F(neighb_2)
    print(neighb_1,neighb_2)

    if f_neighb_2 >= f_Cur_Val and f_neighb_1 <= f_Cur_Val:
        Cur_Val = neighb_2

    elif f_neighb_1 >= f_Cur_Val and f_neighb_2 <= f_Cur_Val:
        Cur_Val = neighb_1

    elif f_neighb_1 <= f_Cur_Val and f_neighb_2 <= f_Cur_Val:
        print("Soln is " + str(Cur_Val))
        break


#Soln is 2.000000000000016
