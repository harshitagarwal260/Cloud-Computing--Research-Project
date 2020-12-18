import Edge_Affinity
import random
def Placement(Set_of_application_selected_for_placing):
    No_of_Instances = int(input("Enter No of Instances"))
    Instances = []
    for i in range(No_of_Instances):
        # downlink speed, Processing Speed, uplink Speed
        Instances.append([random.uniform(4, 20), random.randint(300, 1300), random.uniform(2, 14)])
    P = []
    for i in range(len(Set_of_application_selected_for_placing)):
        t = Edge_Affinity.Applications.index(Set_of_application_selected_for_placing[i])
        tpq =[]
        for j in range(len(Instances)):
            tpq1 = Edge_Affinity.Average_input_data_Size[t]/Instances[j][0]
            tpqe = Edge_Affinity.No_of_Instruction[t]/Instances[j][1]
            tpqo = Edge_Affinity.Output_data_size[t]/Instances[j][2]
            tpq.append(tpq1+tpqe+tpqo)
        q = tpq.index(min(tpq))
        P.append((Set_of_application_selected_for_placing[i],Instances[q]))
        print("Placement is done",P)
        del(Instances[q])


def Selection(Non_dominant_application):
    print("Non_Dominant_application",Non_dominant_application)
    Set_of_application_selected_for_placing = []
    Count_selected_application = 0
    k = False
    Pcg = int(input("No of Allowable Application"))
    for i in range(len(Non_dominant_application)):
        if Count_selected_application + len(Non_dominant_application) <= Pcg:
            Count_selected_application = Count_selected_application + len(Non_dominant_application)
            for i in range(len(Non_dominant_application)):
                Set_of_application_selected_for_placing.append(Non_dominant_application[i])
        else:
            k = True
            break

    if k == True:
        Non_dominant_application.sort(key=lambda x: min(x))
        for q in Non_dominant_application:
            if Count_selected_application + 1 <= Pcg:
                Count_selected_application = Count_selected_application + 1
                Set_of_application_selected_for_placing.append(q)
    print("Set of application",Set_of_application_selected_for_placing)
    Placement(Set_of_application_selected_for_placing)
Non_dominant_application = []
Set_of_Application_for_placement=[]
Set_of_Application_for_placement = Edge_Affinity.Applications
print(Set_of_Application_for_placement)
Set_of_Application_that_Dominant_Application=[]
Set_of_Application_Dominant_By_application=[]
for q in Set_of_Application_for_placement:
    r = []
    No_of_aplication_that_dominate_Application = 0
    for q1 in Set_of_Application_for_placement:
        if (q[0]<q1[0] and q[1]<=q1[1] and q[2]<=q1[2]) or (q[0]<=q1[0] and q[1]<q1[1] and q[2]<=q1[2]) or (q[0]<=q1[0] and q[1]<=q1[1] and q[2]<q1[2]):
            r.append(q1)
        elif (q[0]>q1[0] and q[1]>=q1[1] and q[2]>=q1[2]) or (q[0]>=q1[0] and q[1]>q1[1] and q[2]>=q1[2]) or (q[0]>=q1[0] and q[1]>=q1[1] and q[2]>q1[2]):
            No_of_aplication_that_dominate_Application = No_of_aplication_that_dominate_Application+1

    if No_of_aplication_that_dominate_Application ==0:
        Non_dominant_application.append(q)
        for i in r:
            Set_of_Application_Dominant_By_application.append(i)
    elif No_of_aplication_that_dominate_Application!=0:
        Set_of_Application_that_Dominant_Application.append(No_of_aplication_that_dominate_Application)
Set_of_Application_Dominant_By_application1 = []
for i in Set_of_Application_Dominant_By_application:
    if i not in Set_of_Application_Dominant_By_application1:
        Set_of_Application_Dominant_By_application1.append(i)
while len(Non_dominant_application)!=0:
    for i in range(len(Set_of_Application_for_placement)):
        for j in range(len(Set_of_Application_Dominant_By_application1)):
            Set_of_Application_that_Dominant_Application[j] = Set_of_Application_that_Dominant_Application[j]-1
            if Set_of_Application_that_Dominant_Application[j]==0:
                Non_dominant_application.append(Set_of_Application_Dominant_By_application1[j])
                if len(Non_dominant_application)==len(Set_of_Application_for_placement):
                    Selection(Non_dominant_application)
