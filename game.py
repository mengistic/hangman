

import os
import random
from colorama import Fore, Style

asciiart = ["" for _ in range(7)]
asciiart[6] = r"""
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⣹⡿⠋⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀ ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀WELCOME TO HANGMAN⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⠀⠀⠀⠀------------------
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀ ⠀⠀           
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀     Press [Enter] to start
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀     [q]     to quit
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀Rules:
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀ + guess one letter at a time
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀ + do not guess same letter twice
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣸⣿⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁
"""

asciiart[5] = r"""
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⣹⡿⠋⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀ ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀ ⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣸⣿⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁
"""


asciiart[4] =r"""
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀4 life remaining⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⣹⡿⠋⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠛⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⣀⣠⣼⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣸⣿⣀⣀⣀⡀⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀
"""



asciiart[3] = r"""
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀3 life remaining⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⣹⡿⠋⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠛⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⣀⣠⣼⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⠾⣿
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣸⣿⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

asciiart[2]= r"""
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀2 life remaining⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⣹⡿⠋⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠛⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⣀⣠⣼⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⠾⣿⠷⢶⣤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⣿⠀⠀⠈⠉⠛⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀
⠀⠀⠀⠀⠀⠀⢸⣿
⠀⠀⠀⣀⣀⣀⣸⣿⣀⣀⣀⡀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁
"""


asciiart[1] = r"""
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀  Last chance⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⣹⡿⠋⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠛⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⣀⣠⣼⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⠾⣿⠷⢶⣤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⣿⠀⠀⠈⠉⠛⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀
⠀⠀⠀⣀⣀⣀⣸⣿⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
asciiart[0] = r"""
⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⣹⡿⠋⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠛⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⣀⣠⣼⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⠾⣿⠷⢶⣤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⣿⠀⠀⠈⠉⠛⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠘⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣸⣿⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""



wordlist = (
    "apple", "orage", "green", "hello",
    "the","be","to","of","and",
    "art","in","that","have","I",
    "it","for","not","on","with",
    "he","as","you","do","at",
    "this","but","his","by","from",
    "they","we","say","her","she",
    "or","an","will","my","one",
    "all","would","there","their","is",
    "are","was","were","been","being",
    "had","has","did","can","could",
    "should","may","might","must","who",
    "what","which","when","where","why",
    "how","many","much","more","most",
    "some","such","no","nor","only",
    "own","same","so","than","too",
    "very","just","also","back","after",
    "use","two","first","well","way",
    "even","new","want","because","any",
    "these","give","day","work","look",
    "try","leave","call","good","great",
    "small","large","long","short","high",
    "different","important","public","able","early",
    "young","old","right","left","next",
    "last","few","every","other","another",
    "place","time","year","week","today",
    "people","person","man","woman","child",
    "life","world","hand","eye","head",
    "home","house","room","door","window",
    "school","career","job","office","business",
    "money","service","problem","question","answer",
    "system","program","number","group","company",
    "government","state","country","city","community",
    "family","friend","parent","brother","sister",
    "fact","idea","point","case","issue",
    "information","research","study","story","example",
    "change","move","play","run","stand",
    "turn","start","stop","keep","let",
    "seem","help","talk","hear","feel",
    "bring","happen","write","provide","sit",
    "hold","believe","include","continue","remain"
)



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def display(life, renderword):
    clear()
    print(asciiart[life])
    print("\n\t", " ".join(renderword), "\n")
    
def winthegame():    
    print("YOU WIN!!!")
    input("Press Enter to go back to menu.")
    clear()

    
def losethegame():
    print("You lose :( ")
    input("Press Enter to go back to menu.")
    clear()



def print_colored_letters(colors, letters):
  for i in range(len(letters)):
    print(colors[i] + letters[i], end="")
  print(Style.RESET_ALL)
  
def startgame():
    isWinning = False
    life = 5
    hiddenword = random.choice(wordlist)
    length = len(hiddenword)
    remainslot = len(hiddenword)
    renderword = ["_" for i in range(length)]


    qwerty = "qwertyuiop\nasdfghjkl\nzxcvbnm"
    colors = [Fore.WHITE for i in range(len(qwerty))]


    ### game loop
    while life>0:
        if remainslot==0:
            isWinning=True
            break

        display(life, renderword)
        print_colored_letters(colors, qwerty)
        guess = input("Guess the letter: ")
        our_guess = False

        if guess!="":
            for i in range(length):
                if guess==hiddenword[i]:
                    our_guess = True
                    remainslot = remainslot - 1
                    renderword[i] = guess
            if our_guess==False:
                life = life-1

        ## determine how to print the qwerty keyboard
        for i in range(26):
          if guess == qwerty[i]:
            colors[i] = Fore.GREEN if our_guess else Fore.RED



    ### displaying win/lose message
    display(life, renderword)
    if isWinning: winthegame()
    else:
        print(f"The hidden word is: {hiddenword}")
        losethegame()
    
    
### --------------------
### User Interface
### --------------------
gameOn = True
while gameOn:
    clear()
    print(asciiart[6])
    
    userinput = input("Press Enter/q: ")
    clear()

    if userinput=="": startgame()
    elif userinput == "q": gameOn=False
    else:
        print(f"The input '{userinput}' is not recognized. Exit.")
        gameOn=False



    



