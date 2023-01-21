users = {
    "vlaspet": {
        "first": "Petro",
        "last": "Vlasenko"
    },
    "yana": {
        "first": "Yana",
        "last": "Opanasenko"
    }
}

# for user_name, data in users.items():
#     print(user_name)
#     print(f"{data['first'].title()} {data['last'].title()}\n")

def petro(fuck="petro"):
    print(fuck)

petro()

def p(*petro):
    for x in petro:
        print(x)

p("hi", "fuck you", "skaun")

def y(**yana):
    for x, y in yana.items():
        print(f"x: {x} and y: {y}")

y(fuck="fuck you", team="team up")

from collections import OrderedDict

f = OrderedDict()

f["petro"] = None
f["yana"] = None
f["anton"] = None
f["bob"] = None

for x in f.keys():
    print(x)

"petro\n".rstrip()

try:
    answer = int(5) / int(1)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)