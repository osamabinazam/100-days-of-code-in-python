

# Finding combinations of letters
def combination_of_letter (dictionary):
    values = list (dictionary.values())
    count=0;
    for i in values[count]:
        for j in values[count+1]:
            for k in values[count+2]:
                print(i+j+k)

my_dict = {
    1:["a","b"],
    2:["c","d"],
    3:["e","f"]
}
combination_of_letter(my_dict)