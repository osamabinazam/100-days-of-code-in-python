# Concatenating three dictionaries to forma a single dictionary

# Represent top 3 students in maths
maths_students = {
    1: ["Osama" , 22, 'A'],
    2: ["Shafique" , 20,'B' ],
    3: ["Shahzaman" , 21,'B']
}

# Represent top 3 students in english
cs_students = {
    4: [ "Maria", 21,'A' ],
    5: [ "Izzah", 22,'B' ],
    6: ["Ayesha" , 21,'C']
}

# Represent top 3 students in BBA
bba_students = {
    7: [ "Nehal", 23,'A' ],
    8: [ "Hassan", 22,'B' ],
    9:["Zahid",23,'B']
}

# Represent the topers of nthp_19
nthp_19_toppers = {}

# Concatenating three dictionaries to forma a single dictionary
for dict in (maths_students,cs_students,bba_students) :
    nthp_19_toppers.update(dict)

print("\nToppers of NTHP 19 are given below : ")
for key,student in nthp_19_toppers.items():
    print ("Student ID: " , key, ": \nName: ", student[0], " Age: ", student[1])
    print("")
    # temp_str="Name"
    # count=0
    # for value in student:
    #     print(f"{temp_str} :",value)
    #     count =(count+1)
    #     if count ==1:
    #         temp_str="Age"
    #     elif count == 2:
    #         temp_str="Section"