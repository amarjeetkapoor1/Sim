#***********************************************************************
#*                                                                     *
#*   File:                                                             *
#*       joints_old.py                                                 *
#*                                                                     *
#*   Author:                                                           *
#*      Amritpal Singh <amrit3701@gmail.com>                           *
#*                                                                     *
#*   Brief:                                                            *
#*      This program file contain FreeCAD macros.                      *
#*                                                                     *
#***********************************************************************

import mysql.connector`

cnx=mysql.connector.connect(user='root',password='a', database='Sim')

cursor=cnx.cursor()

query = ("select idd,x,y,z from Joint;")

cursor.execute(query)

a=[]

for i in cursor:
    a.append(i)

[(1, 0.0, 0.0, 0.1), (2, 5, 0.0, 0.0), (3, 10.0, 0.0, 0.0), (5, 10.0, 0.0, 10.0), (6, 5, 0.0, 10.0), (7, 0.0, 0.0, 10.0), (8, 0.0, 0.0, 5), (9, 5, 0.0, 5), (10, 10.0, 0.0, 5.0), (11, 0.0, 5, 0.0), (12, 5, 5, 0.0), (13, 10.0, 5, 0.0), (14, 10.0, 5, 10.0), (15, 5, 5, 10.0), (16, 0.0, 5, 10.0), (17, 0.0, 5, 5), (18, 5, 5, 5), (19, 10.0, 5, 5.0), (20, 0.0, 10.0, 0.0), (21, 5, 10.0, 0.0), (22, 10.0, 10.0, 0.0), (23, 10.0, 10.0, 10.0), (24, 5, 10.0, 10.0), (25, 0.0, 10.0, 10.0), (26, 0.0, 10.0, 5), (27, 5, 10.0, 5), (28, 10.0, 10.0, 5.0), (29, 0.0, 15.0, 0.0), (30, 5, 15.0, 0.0), (31, 10.0, 15.0, 0.0), (32, 10.0, 15.0, 10.0), (33, 5, 15.0, 10.0), (34, 0.0, 15.0, 10.0), (35, 0.0, 15.0, 5), (36, 5, 15.0, 5), (37, 10.0, 15.0, 5.0), (38, 0.0, 20.0, 0.0), (39, 5, 20.0, 0.0), (40, 10.0, 20.0, 0.0), (41, 10.0, 20.0, 10.0), (42, 5, 20.0, 10), (43, 0.0, 20.0, 10.0), (44, 0.0, 20.0, 5), (45, 5, 20.0, 5), (46, 10.0, 20.0, 5.0)]

joints = dict()
for i in range(len(a)):
   val=a[i][0]
   temp=[]
   for j in range(1,4):
       temp.append(a[i][j])
   joints[a[i][0]] = temp


cursor2=cnx.cursor()
query2 = ("select member_id, group_concat(joint_id SEPARATOR ', ') as joint_id from Member_incidence group by Member_incidence.member_id;")
cursor2.execute(query2)

b=[]

for i in cursor2:
    b.append(i)

for i in range(0,len(c)):
    for j in range(0, len(a)):
            if a[j][0]==c[i][1]:
                    start_pt=FreeCAD.Vector(a[j][1],a[j][2],a[j][3])
            if a[j][0]==c[i][2]:
                    end_pt=FreeCAD.Vector(a[j][1],a[j][2],a[j][3])
    Points=[start_pt,end_pt]
    Draft.makeWire(Points,closed=False,face=True,support=None)



c=[(17, 1, 11), (18, 2, 12), (19, 3, 13), (20, 5, 14), (21, 6, 15), (22, 7, 16), (23, 8, 17), (24, 9, 18), (25, 10, 19), (26, 11, 12), (27, 12, 13), (28, 13, 19), (29, 14, 15), (30, 15, 16), (31, 16, 17), (32, 11, 17), (33, 17, 18), (34, 18, 19), (35, 15, 18), (36, 12, 18), (37, 14, 19), (38, 11, 20), (39, 12, 21), (40, 13, 22), (41, 14, 23), (42, 15, 24), (43, 16, 25), (44, 17, 26), (45, 18, 27), (46, 19, 28), (47, 20, 21), (48, 21, 22), (49, 22, 28), (50, 23, 24), (51, 24, 25), (52, 25, 26), (53, 20, 26), (54, 26, 27), (55, 27, 28), (56, 24, 27), (57, 21, 27), (58, 23, 28), (59, 20, 29), (60, 21, 30), (61, 22, 31), (62, 23, 32), (63, 24, 33), (64, 25, 34), (65, 26, 35), (66, 27, 36), (67, 28, 37), (68, 29, 30), (69, 30, 31), (70, 31, 37), (71, 32, 33), (72, 33, 34), (73, 34, 35), (74, 29, 35), (75, 35, 36), (76, 36, 37), (77, 33, 36), (78, 30, 36), (79, 32, 37), (80, 29, 38), (81, 30, 39), (82, 31, 40), (83, 32, 41), (84, 33, 42), (85, 34, 43), (86, 35, 44), (87, 36, 45), (88, 37, 46), (89, 38, 39), (90, 39, 40), (91, 40, 46), (92, 41, 42), (93, 42, 43), (94, 43, 44), (95, 38, 44), (96, 44, 45), (97, 45, 46), (98, 42, 45), (99, 39, 45), (100, 41, 46)]


from math import sqrt,pow

def make_box(name, length, width, height, base_vector, base_rotation):
        ac_doc = FreeCAD.ActiveDocument
        ac_doc.addObject("Part::Box",name)
        getattr(ac_doc, name).Length = length
        getattr(ac_doc, name).Width = width
        getattr(ac_doc, name).Height = height
        getattr(ac_doc, name).Placement=Base.Placement(Base.Vector(base_vector[0],base_vector[1],base_vector[2]),Base.Rotation(base_rotation[0],base_rotation[1],        base_rotation[2],base_rotation[3]))



dim1=.5
dim2=.5

for i in range(0,len(c)):
    for j in range(0, len(a)):
            if a[j][0]==c[i][1]:
                    j1=j
            if a[j][0]==c[i][2]:
                    j2=j

    dis = sqrt(pow((a[j2][1]-a[j1][1]),2)+pow((a[j2][2]-a[j1][2]),2)+pow((a[j2][3]-a[j1][3]),2))

    if (a[j2][1]-a[j1][1]) != 0:
        nam = "beam_xaxis"+str(i)
        if a[j2][1] > a[j1][1]:
            make_box(nam, dis, dim1, dim2, [a[j1][1]+.25,a[j1][2],a[j1][3]], [0, 0, 0, 1])
        else:
            make_box(nam, dis, dim1, dim2, [a[j2][1]+.25,a[j2][2],a[j2][3]], [0, 0, 0, 1])

    if (a[j2][2]-a[j1][2]) != 0:
        nam = "column_yaxis"+str(i)
        if a[j2][2] > a[j1][2]:
            make_box(nam, dim1, dis, dim2, [a[j1][1],a[j1][2]+.25,a[j1][3]], [0, 0, 0, 1])
        else:
            make_box(nam, dim1, dis, dim2, [a[j2][1],a[j2][2]+.25,a[j2][3]], [0, 0, 0, 1])

    if (a[j2][3]-a[j1][3]) != 0:
        nam = "beam_zaxis"+str(i)
        if a[j2][3] > a[j1][3]:
            make_box(nam, dim1, dim2, dis, [a[j1][1],a[j1][2],a[j1][3]+.25], [0, 0, 0, 1])
        else:
            make_box(nam, dim1, dim2, dis, [a[j2][1],a[j2][2],a[j2][3]+.25], [0, 0, 0, 1])

# Initialise a dictionary
mem_incidence = dic()
# Iterate from 0 to len of a
for i in range(0,len(a)):
    temp=[]
    # Storing the value of the key for dictionary
    val=a[i][0];
    for j in range(0,len(a)):
        # Check if val is equal to another key i.e "a[j][0]"
        if val == a[j][0]:
            # Append the value of the key in temp
            temp.append(a[j][1]);
    # Append key (val) and value (temp in dictionary)
    mem_incidence[val]=temp


