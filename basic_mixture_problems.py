print("\nPart 1 Enter the Resource Constraints as Inequalities in Standard Form\n")

user_input_x = input("Enter the value that x is always greater then or equal to: ")

user_input_y = input("Enter the value that y is always greater then or equal to: ")

list_count = 0
flag = True
m_list = []
b_list = []
x_intersection_list = []
y_intersection_list = []


while flag == True:
   user_input_a = input("Enter the x coefficient of the inequality: ")
   user_input_b = input("Enter the y coefficient of the inequality: ")
   user_input_c = input("Enter the max of the inequality: ")
   m = ((int(user_input_a)*-1)/(int(user_input_b)))
   b = ((int(user_input_c))/(int(user_input_b)))
   x_intersection = ((int(m)*int(user_input_x))+int(b))
   y_intersection = ((int(user_input_y)-int(b))/int(m))
   m_list.append(m)
   b_list.append(b)
   x_intersection_list.append(x_intersection)
   y_intersection_list.append(y_intersection)
   list_count += 1
   user_input_flag = input("If you don't have any more inequalities to add enter N to stop looping: ")
   if user_input_flag == "N":
#       print(str(m_list) + str(b_list) + str(x_intersection_list) + str(y_intersection_list)) #Debugging info
       flag = False

num_inc_1 = 0
x_point_list = []
y_point_list = []
point_list_count = 0


while num_inc_1 != list_count:
   m1 = m_list[num_inc_1]
   b1 = b_list[num_inc_1]
   num_inc_2 = num_inc_1
   while num_inc_2 != (list_count - 1):
       m2 = m_list[num_inc_2 + 1]
       b2 = b_list[num_inc_2 + 1]
       x_point = (b1-b2) / (m2-m1)
       y_point = m1 * x_point + b1
       x_point_list.append(x_point)
       y_point_list.append(y_point)
       point_list_count += 1
       num_inc_2 += 1
   num_inc_1 += 1

#print(str(x_point_list) + str(y_point_list)) #Debugging info

print("\nPart 2 Enter the Objective Function (the function to be optimized)\n")

x_coe = input("Enter the x coefficient: ")
y_coe = input("Enter the y coefficient: ")

objective_list = []
objective_list_count = 0

num_inc_3 = 0

while num_inc_3 != list_count:
    x_intersection_2 = x_intersection_list[num_inc_3]
    objective_value = (int(x_intersection_2) * int(x_coe))
    objective_list.append([str(objective_value), str(x_intersection_2), str(user_input_x)])
    objective_list_count += 1
    num_inc_3 += 1

num_inc_4 = 0

while num_inc_4 != list_count:
    y_intersection_2 = y_intersection_list[num_inc_4]
    objective_value = (int(y_intersection_2) * int(y_coe))
    objective_list.append([str(objective_value), str(user_input_y), str(y_intersection_2)])
    objective_list_count += 1
    num_inc_4 += 1

num_inc_5 = 0

while num_inc_5 != (list_count - 1):
    x_point_2 = x_point_list[num_inc_5]
    y_point_2 = y_point_list[num_inc_5]
    objective_value = ((int(x_point_2) * int(x_coe)) + (int(y_point_2) * int(y_coe)))
    objective_list.append([str(objective_value), str(x_point_2), str(y_point_2)])
    objective_list_count += 1
    num_inc_5 += 1

#print(str(objective_list)) #Debugging info

num_inc_6 = 0

print("\nThe format for the following arrays is first the objective value (highest value best value) and then the point so (x value, y value)\n")
 
while num_inc_6 != objective_list_count:
    print(objective_list[num_inc_6])
    num_inc_6 += 1
