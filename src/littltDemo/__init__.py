from pip._vendor.distlib.compat import raw_input

name = raw_input("what is your name?")
if name.endswith("tank"):
    print("hello tank !")
else:
    print(name + " You are welcome !")
