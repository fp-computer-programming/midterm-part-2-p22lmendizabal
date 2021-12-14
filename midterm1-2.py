# author: LM (AMDG) 12/14/21
initial_v = float(input("Enter the initial velocity: "))
final_v = float(input("Enter the final veloccity: "))
total_time = int(input("Enter the amount of time: "))


def acceleration(initial, final, time):
    a = (final - initial) / time
    return a


average_a = acceleration(initial_v, final_v, total_time)
print("The average velocity is {0} meters per second".format(average_a))
