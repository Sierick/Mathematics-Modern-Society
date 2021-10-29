points_list = []
m_b_list = []
x_values_list = []
y_values_list = []
flag = True

print("\nEnter the Resource Constraints as Inequalities in Standard Form\n")

user_input_x = input("Enter the value that x is always greater then or equal to: ")

user_input_y = input("Enter the value that y is always greater then or equal to: ")

points_list.append([user_input_x, user_input_y])

while flag == True:
   user_input_a = input("Enter the x coefficient of the inequality: ")
   user_input_b = input("Enter the y coefficient of the inequality: ")
   user_input_c = input("Enter the max of the inequality: ")
   if float(user_input_b) != 0:
      m = ((float(user_input_a)*-1)/(float(user_input_b)))
      b = ((float(user_input_c))/(float(user_input_b)))
   else:
      m = (float(user_input_a)*-1)
      b = float(user_input_c)
   m_b_list.append([m, b])
   y_value_of_vertical_line_intersection_point = ((float(m)*float(user_input_x))+float(b))   
   y_values_list.append(y_value_of_vertical_line_intersection_point)
   if float(m) != 0:
      x_value_of_horizontal_line_intersection_point = ((float(user_input_y)-float(b))/float(m))
   else:
      x_value_of_horizontal_line_intersection_point = (float(user_input_y)-float(b))
   x_values_list.append(x_value_of_horizontal_line_intersection_point)
   user_input_flag = input("If you don't have any more inequalities to add enter N to stop looping: ")
   if user_input_flag == "N":
       flag = False

min_x_value = min(x_values_list)
points_list.append([min_x_value, user_input_y])

min_y_value = min(y_values_list)
points_list.append([user_input_x, min_y_value])

num_inc_1 = 0
point_list_count = 0

while num_inc_1 != len(m_b_list):
   m1 = float(m_b_list[num_inc_1][0])
   b1 = float(m_b_list[num_inc_1][1])
   num_inc_2 = num_inc_1
   while num_inc_2 != (len(m_b_list) - 1):
       m2 = float(m_b_list[num_inc_2 + 1][0])
       b2 = float(m_b_list[num_inc_2 + 1][1])
       x_point = float((b1-b2) / (m2-m1))
       y_point = float(m1 * x_point + b1)
       points_list.append([x_point, y_point])
       point_list_count += 1
       num_inc_2 += 1
   num_inc_1 += 1

print("\nEnter the Objective Function (the function to be optimized)\n")

x_coe = input("Enter the x coefficient: ")
y_coe = input("Enter the y coefficient: ")

objective_list = []
num_inc_3 = 0

while num_inc_3 != (len(points_list)):
    x_point_2 = points_list[num_inc_3][0]
    y_point_2 = points_list[num_inc_3][1]
    objective_value = ((float(x_point_2) * float(x_coe)) + (float(y_point_2) * float(y_coe)))
    objective_list.append([objective_value, x_point_2, y_point_2])
    num_inc_3 += 1

num_inc_4 = 0

print("\nThe format for the following arrays is first the objective value (highest value best value) and then the point so (x value, y value)\n")
 
while num_inc_4 != len(objective_list):
    print(objective_list[num_inc_4])
    num_inc_4 += 1
