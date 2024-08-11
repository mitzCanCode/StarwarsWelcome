import rainbowtext
from random import choice, randint

at_at = "               ________\n          _,.-Y  |  |  Y-._\n      .-~\"   ||  |  |  |   \"-.\n      I\" \"\"==\"|\" !\"\"! \"|\"[]\"\"|     _____\n      L__  [] |..------|:   _[----I\" .-{\"-.\n     I___|  ..| l______|l_ [__L]_[I_/r(=}=-P\n    [L______L_[________]______j~  '-=c_]/=-^\n     \\_I_j.--.\\==I|I==_/.--L_]\n       [_((==)[`-----\"](==)j\n          I--I\"~~\"\"\"~~\"I--I\n          |[]|         |[]|\n          l__j         l__j\n          |!!|         |!!|\n          |..|         |..|\n          ([])         ([])\n          ]--[         ]--[\n          [_L]         [_L] \n         /|..|\\       /|..|\\\n        `=}--{='     `=}--{='\n       .-^--r-^-.   .-^--r-^-.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

darth_vader = """
                       .-.
                      |_:_|
                     /(_Y_)\\
.                   ( \\ M// )
 '.               _.''/'-'\\''._
   ':            /.--'[[[[]'--.\\
     ':        /_'  : |::'| :  '.\\
       ':     //   ./ |oUU| \\'  :\\
         ':  _:'..' \\ |___|_/ :   :|
           ':.  .'  |_[___]_|  :.':\\
            [::\\ |  :  | |  :   ; : \\
             '-'   \\ .| |.' \\ .;.' |
             |\\    \\ '-'   :       |
             |  \\   \\.:    :   |   |
             |   \\  |  '.   :    \\ |
             /       \\  :. .;       |
            /     |   |  :__/     :  \\
           |  |   |    \\   | \\  |   ||
          /   \\  : :  |:   /  |__|   /|
          |     : : :_/_|  /'._\\  '--|_\\
          /___.-/_|-'   \\  \\

"""

boba_fett = """
⢀⣀⣀⡀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀
⠈⢹⠉⢁⣴⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⠀⢸⠀⣾⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⡀⠀
⠀⣾⢀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⡀⠀
⠀⣿⣤⣀⠈⠉⠉⢻⣿⡟⠉⠉⠉⣀⣤⠀
⠀⠀⣿⣿⣷⣄⠀⢸⣿⡇⠀⢠⣾⣿⣿⡀
⠀⢰⣿⣿⣿⣿⡆⢸⣿⡇⢠⣿⣿⣿⣿⡇
⠀⠈⠙⠻⢿⣿⣿⢸⣿⡇⣸⣿⡿⠟⠋⠁
⠀⠀⠀⠀⠀⠈⠉⠈⠉⠁⠉⠁⠀⠀⠀⠀
"""


death_star = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣻⣿⣿⣿⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣡⣶⣿⣷⣶⣍⠻⣿⣿⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣷⡙⣿⣿⡆⠀
⠀⠀⠀⠤⠤⠤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⡟⢻⣿⣿⣿⣇⢹⣿⣿⡄
⠀⢰⡄⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢻⣿⣿⣿⣿⣿⣿⡟⣸⣿⣿⣇
⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⠿⣿⣿⣿⠟⣱⣿⣿⣿⣿
⣭⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⡿⢟⣫⣷
⠈⢻⡿⣶⣾⣭⣽⣛⣛⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣛⣛⣻⣭⣽⣷⣶⣿⣿⣿⡏
⠀⠈⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠈⠉⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
⠀⠀⠀⠀⠈⢉⣉⣩⣭⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠛⣛⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀
"""

tie_fighter = """
⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀
⠀⢸⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⡿⢟⣛⣛⣛⣛⡿⢿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀
⢠⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣿⣿⣿⣿⣿⣿⡿⠫⣾⣿⣿⣿⢿⣿⣿⣷⠝⢿⣿⣿⣿⣿⣿⣆⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⡀
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾⣿⡮⣫⣷⣾⣶⣮⡝⢱⣾⣷⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣄⣀⣀⢀⣠⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣿⣿⣿⣿⠘⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣿⣿⣆⢿⣿⣿⣿⣿⡟⣰⣿⣿⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣿⢟⣵⣮⣭⣭⣵⣮⡻⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠙⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⣿⣿⣿⣿⣿⣿⣿⣷⣽⣻⠿⠿⠿⠿⣟⣫⣾⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⡟
⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡏⠀
⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⠿⣿⣿⣿⣿⣿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀
⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡇⠀
⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀
⠀⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀
⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀
"""


darth_vader2 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣯⠪⣕⢶⣦⣔⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣧⡙⣧⢹⣿⣷⣇⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⡟⠛⢿⣾⢿⡟⠟⢛⡄⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⢟⣯⢖⣒⣚⣭⠀⣣⣈⡨⣢⠀⠀
⠀⠀⠀⣿⣿⣿⢏⡛⠱⢿⣧⣿⢿⡂⠻⠭⠿⣴⠀⠀
⠀⠀⣰⣿⣿⡟⢼⣿⡶⡄⣴⣶⣶⠇⠀⢶⣶⡎⡗⠀
⠀⢠⣿⣿⣿⢇⣷⣭⣃⠈⠙⠁⣠⢟⡟⡷⡙⢸⣷⠃
⢀⣿⣿⠿⢟⣸⣷⠶⠯⠍⠀⡫⢬⣬⣤⣥⡅⣊⣿⣼
⡜⣫⣴⣿⣿⣿⠁⢰⣿⣿⣿⣿⣞⠿⢛⣵⣾⡿⠛⠁
⠙⠿⠿⠿⣿⣿⣼⣬⣿⣿⣿⣿⣿⣷⠟⠉⠁⠀⠀⠀
"""

stormtrooper ="""

           ,ooo888888888888888oooo,
         o8888YYYYYY77iiiiooo8888888o
        8888YYYY77iiYY8888888888888888
       [88YYY77iiY88888888888888888888]
       88YY7iYY888888888888888888888888
      [88YYi 88888888888888888888888888]
      i88Yo8888888888888888888888888888i
      i]        ^^^88888888^^^     o  [i
     oi8  i           o8o          i  8io
   ,77788o ^^  ,oooo8888888ooo,   ^ o88777,
   7777788888888888888888888888888888877777
    77777888888888888888888888888888877777
     77777788888888^7777777^8888888777777
     88888778888^7777ooooo7777^8887788888
    88888888888888888888888888888888888887
     78888887788788888^;;^888878877888887
      7888878^ ^8788^;;;;;;^878^ ^878877
        777888o8888^;ii;;ii;^888o87777
  """


dark_side_quotes = [
    "Give yourself to the dark side.",
    "Power! Unlimited power!",
    "I find your lack of faith disturbing.",
    "You don't know the power of the dark side!",
    "Join me, and together we can rule the galaxy as father and son.",
    "The dark side of the Force is a pathway to many abilities some consider to be unnatural.",
    "You are unwise to lower your defenses!",
    "You will find that it is you who are mistaken, about a great many things.",
    "Your feeble skills are no match for the power of the dark side!",
    "Now, young Skywalker, you will die.",
    "The Emperor is not as forgiving as I am.",
    "It is your destiny. Join me and complete your training.",
    "Your hatred has made you powerful. Now, fulfill your destiny and take your father's place at my side!",
    "The Force is strong with you. A powerful Sith you will become.",
    "Your father was weak. I have destroyed him.",
    "I will show you the true nature of the Force.",
    "Soon, you will learn to appreciate my power.",
    "You were the chosen one! It was said that you would destroy the Sith, not join them!",
    "I have been waiting for this day for a long time.",
    "The Sith will rise again!",
    "Your rage has made you strong. Use that strength to serve the dark side.",
    "I will make you suffer as I have suffered.",
    "Embrace your hatred, and you will become more powerful than you can imagine.",
    "The dark side is the pathway to victory.",
    "The end of the Jedi is near. It is inevitable.",
    "I have seen your future, and I have altered it.",
    "Do not underestimate the power of the dark side.",
    "You are no match for the power of the Sith.",
    "The power of the dark side will make you invincible.",
    "Everything you know is about to change.",
    "You will never escape your destiny.",
    "Feel the power of the dark side course through you.",
    "You are weak, and you will be destroyed.",
    "The dark side is seductive. Surrender to it.",
    "The Sith are the true rulers of the galaxy.",
    "Your fate is sealed.",
    "The power of the dark side is absolute.",
    "You have already lost.",
    "The galaxy will bow before me.",
    "I will bring order to the galaxy through the power of the dark side.",
    "You will serve me or face destruction.",
    "The dark side is the path to ultimate power.",
    "The Sith will bring balance to the Force through power.",
    "Your destiny is to serve the dark side.",
    "The end of the Jedi is inevitable. Their extinction is at hand.",
    "You will come to realize the true power of the dark side.",
    "Your struggle is futile. Surrender to the dark side."
]


RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[97m'
RESET = '\033[0m'


dark_side = [f"{WHITE}{at_at}", f"{RED}{darth_vader}", f"{RED}{darth_vader2}", f"{WHITE}{stormtrooper}",f"{GREEN}{boba_fett}", f"{GREEN}{tie_fighter}", f"{GREEN}{death_star}"]

char_decision = choice(dark_side)
quote = choice(dark_side_quotes)

print(f"{RED}{char_decision}")
print(f"{quote}{RESET}")
