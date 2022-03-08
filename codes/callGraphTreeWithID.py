import re
from treelib import Node, Tree

with open("cg.txt") as file:
    lines = file.readlines()

with open("APICalls.txt") as file2:
    APIlines = file2.readlines()

def get_API_id(text):
    for r in range(len(APIlines)):
        if text in APIlines[r]:
            api = APIlines[r].split(" ")
            return api[0]

def build_product_tree():
    text_arr = []
    text2_arr = []
    root_arr = []

    for i in range(len(lines)):
        counter = 0
        if "Children of" in lines[i]:
            text = re.split('<|>', str(lines[i]))
            for j in range(len(lines)):
                if text[1] in lines[j]:
                    counter += 1
                    if counter == 2:
                        break

            if counter < 2:
                if not(((i+1) < len(lines)) and ("Children of" in lines[i+1])):
                    tree = Tree()
                    tree.create_node(text[1], get_API_id(text[1]))
                    text_arr.append(text[1])
                    root_arr.append(tree)

    for x in range(30):
        for s in range(len(lines)):
            for y in range(len(text_arr)):
                if "Children of <"+text_arr[y] in lines[s]:
                    if (s+1) < len(lines):
                        z = s + 1
                    else:
                        break
                    while not("Children of" in lines[z]):
                        text2 = re.split('<|>', str(lines[z]))
                        text2_arr.append(text2[1])

                        for c in range(len(root_arr)):
                            if root_arr[c].contains(get_API_id(text_arr[y])):
                                root = root_arr[c]
                        leaf = root.create_node(text2[1], get_API_id(text2[1]), parent=get_API_id(text_arr[y]))
                        if (z+1) < len(lines):
                            z += 1
                        else:
                            break
        text_arr = text2_arr
        text2_arr = []

    #for z in range(len(root_arr)):
        #root_arr[z].show()
        #print("\n")

    #print(len(root_arr))
    file2.close()
    return root_arr

def get_sequences(arr):
    count = 0
    with open("b44.txt", "a") as file3:
        file3.seek(0)

        for q in range(len(arr)):
            seq_arr_arr = arr[q].paths_to_leaves()
            for p in range(len(seq_arr_arr)):
                count += 1
                file3.write(str(count) + " ")
                for t in range(len(seq_arr_arr[p])):
                    if t == len(seq_arr_arr[p])-1:
                        file3.write(str(seq_arr_arr[p][t]))
                    else:
                        file3.write(str(seq_arr_arr[p][t])+"-->")
                file3.write("\n")

if __name__ == '__main__':
    root_arr = build_product_tree()
    get_sequences(root_arr)
    file.close()
