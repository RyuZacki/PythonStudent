def decor(func):
    def wrap():
        print('============')
        func()
        print('============')
    return wrap

@decor
def print_text():
    print('Hello world!')

print_text()

add1 = lambda x, y: x + y
print(add1(5, 7))

def sum(x, y):
    c = x + y
    print(c)

print(sum(3, 5))

class animal():
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def a_name(self):
        print(self.name)

    def a_color(self):
        print(self.color)

cat = animal('Borik', 'red')
cat.a_name()
cat.a_color()


from colorama import init, Fore, Back, Style

init()

def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print("                **    **  ********  **        **            **      ")
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **      ")

console_picture()
input()

a = ["Жопа", "Пися", "Гавно"]

print("Жопа" in a)

b = "Жопа"
for i in a:
    if i == b:
        a.append("Привет")

print(len(a))