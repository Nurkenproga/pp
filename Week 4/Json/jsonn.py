import json

with open("sample-data.json", "r") as file:
    sampledata = json.load(file)

print("Interface status")
print("=" * 80)
print("DN", " " * 38, "Description", " " * 3, "Speed", " " * 8, "MTU")
print("-" * 41, "-" * 13, " ", "-" * 6, " " * 6, "-" * 6)
for imdata in sampledata["imdata"]:
    for i in imdata:    
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t", "\t", imdata[i][j]["speed"], "\t", imdata[i][j]["mtu"])