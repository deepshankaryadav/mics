import re
import os

re_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
fl = os.listdir("_directory_name_")

for i in fl:
    with open(i) as fh_in:
        with open("final.txt", "a+") as fh_out:
            for line in fh_in:
                match_list = re_pattern.findall(line)
                if match_list:
                    fh_out.write(match_list[0]+"\r")