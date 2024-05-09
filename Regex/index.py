import re 

ndung = "Hello, I am a Python Developer. I am learning Python."
regex1 = re.compile(r"I(.*?)Python")

kq1 = regex1.search(ndung)
kq2 = regex1.findall(ndung)

print(kq1.group(), kq1.group(1), kq1.groups())
print(kq2)