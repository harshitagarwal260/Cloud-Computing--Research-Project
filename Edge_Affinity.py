import random
N = int(input("Enter No Of Application"))
Applications = []
User_define_deadline= []
User_define_deadline1= []
Average_input_data_Size=[]
Average_input_data_Size1=[]
Sensing_Frequency =[]
Sensing_Frequency1 =[]
No_of_Instruction = []
Output_data_size = []
for i in range(N):
    User_define_deadline.append(random.uniform(0.300,1.5))
    Average_input_data_Size.append(random.uniform(0.3,1.5))
    Sensing_Frequency.append(random.randint(1,8))
for i in User_define_deadline:
    User_define_deadline1.append(abs((i-min(User_define_deadline))/(max(User_define_deadline)-min(User_define_deadline))))
for i in Average_input_data_Size:
    Average_input_data_Size1.append(abs((i-min(Average_input_data_Size))/(max(Average_input_data_Size)-min(Average_input_data_Size))))
for i in Sensing_Frequency:
    Sensing_Frequency1.append(abs((i-min(Sensing_Frequency))/(max(Sensing_Frequency)-min(Sensing_Frequency))))
for i in range(N):
    Applications.append([User_define_deadline1[i],Average_input_data_Size1[i],Sensing_Frequency1[i]])
for i in range(N):
    No_of_Instruction.append(random.randint(300,1300))
for i in range(N):
    Output_data_size.append(random.uniform(0.1,1))
