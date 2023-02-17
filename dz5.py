from colorama import init

init()

from colorama import Fore, Back, Style

print(Fore.RED + 'Робить цей текст червоним')

print(Back.GREEN + 'Робить задній фон зеленим')

print(Style.DIM + 'міняє стиль тексту')

print(Style.RESET_ALL)

print('Вертає все назад')