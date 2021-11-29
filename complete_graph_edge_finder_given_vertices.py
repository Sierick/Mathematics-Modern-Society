vertex_num_user_input = input("Enter the number of vertex: ")
answer = (((float(vertex_num_user_input) - 1)**2) + (float(vertex_num_user_input) - 1)) / 2
print("The number of edges required to create a complete graph with " + str(vertex_num_user_input) + " vertexs is " + str(answer) + " edges.")
