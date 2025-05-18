import os


def main():
    i=0
    path="A:/AI Course Material/Quarter-3/Class Work/Assignment_Projects/Project_4_Assignments/Assignments_01/Bulk File Re-namer Python Project/testfolder/"
    for filename in os.listdir(path):
        my_dest = "imge" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()