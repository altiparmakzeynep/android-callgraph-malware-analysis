import re

from treelib import Node, Tree

with open("cg.txt") as file:
    lines = file.readlines()

with open("APICalls.txt") as file2:
    APIlines = file2.readlines()

class TreeNode:
    def __init__(self, data):   # constructor
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent    # getting level from parent node
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3     # spaces for show leaf's levels
        prefix = spaces +" |" if self.parent else ""

        for z in range(len(APIlines)):
            if self.data in APIlines[z]:
                api = APIlines[z].split(" ")
        print(prefix + api[0])
        if self.children:
            for child in self.children:
                child.print_tree()
        else: 
            print("\n")

    def add_child(self, child):
        child.parent = self
        self.children.append(child)     # add child to the parent


def build_product_tree():
    text_arr = []
    node_arr = []
    text2_arr = []
    node2_arr = []
    root_arr = []

    with open("APICalls.txt", "a+") as file2:
        file2.seek(0)
        APIlines = file2.readlines()

        APIcount = len(APIlines)
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
                        containCount = 0
                        lvl1 = TreeNode(text[1])
                        text_arr.append(text[1])
                        node_arr.append(lvl1)
                        root_arr.append(lvl1)
                        for h in range(len(APIlines)):    
                            if (text[1] in APIlines[h]):
                                containCount +=1
                                break
                        if(containCount == 0):        
                            APIcount += 1
                            file2.write(str(APIcount) +
                                            " " + text[1] + "\n")

        for x in range(30):
            for s in range(len(lines)):
                for y in range(len(text_arr)):
                    if "Children of <"+text_arr[y] in lines[s]:
                        if (s+1) < len(lines):
                            z = s + 1
                        else:
                            break
                        while not("Children of" in lines[z]):
                            containCount2 = 0
                            text2 = re.split('<|>', str(lines[z]))
                            text2_arr.append(text2[1])
                            leaf = TreeNode(text2[1])
                            node2_arr.append(leaf)
                            node_arr[y].add_child(leaf)
                            for d in range(len(APIlines)):    
                                if (text2[1] in APIlines[d]):
                                    containCount2 +=1
                                    break
                            if(containCount2 == 0):        
                                APIcount += 1
                                file2.write(str(APIcount) +
                                            " " + text2[1] + "\n")
                            if (z+1) < len(lines):
                                z += 1
                            else:
                                break

            node_arr = node2_arr        # exchange arrays for moving the next level
            node2_arr = []
            text_arr = text2_arr
            text2_arr = []

    for z in range(len(root_arr)):
        root_arr[z].print_tree()

    print(len(root_arr))
    file2.close()


if __name__ == '__main__':
    build_product_tree()
    file.close()