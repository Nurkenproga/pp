#Write a Python program to convert a given camel case string to snake case.
import re

def f(mObject):
    return mObject.group("g1")+ "_" + mObject.group("g2").lower()


text = "mySuperVar"

pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"

print(re.sub(pattern, f, text))