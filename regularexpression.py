#regular expression

import re

txt="The outside is Raining"
x=re.search("^The.*Raining$",txt)
if x:
    print("yes")
else:
    print("No")


y=re.findall("is",txt)
print(y)


x="my name is vishwa . I am studing 11 th std . my gmail id - vishawa23@gmail.com . currently upgrading my skills in python at ocean academy."
