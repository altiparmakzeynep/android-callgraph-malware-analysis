#/usr/bin/python3 python3
print('== START OF PROGRAM == \n')
# Read First File
print('Reading First File \n')

for a in range(1, 45):
    with open("b/b" + str(a) +".txt", "r") as file_one:
        data_one = file_one.readlines()
    # Read Second File
    print('Reading Second File \n')
    for b in range(a+1, 45):
        with open('b/b' + str(b) + '.txt', 'r') as file_two:
            data_two = file_two.readlines()
        # Write similar data to a file
        print('Write Similar Data to File \n')
        with open('commonNew.txt', 'a') as file_out:
            #Compare the data of two files
            for i in range(len(data_one)):
                data1 = str(data_one[i]).split(" ")
                for j in range(len(data_two)):
                    data2 = str(data_two[j]).split(" ")
                    # Check if data match
                    if (data1[1] == data2[1]):
                        # Write the duplicate data to file
                        file_out.write(data2[1].strip()+'\n')
print('== END OF PROGRAM ==')

