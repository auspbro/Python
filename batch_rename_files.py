#!/usr/bin/python
# -*- coding: utf-8 -*-

# batch_file_rename.py
# Created: 17th August 2018

'''
This will batch rename a group of files in a given directory,
once you pass the current and new keyword.
'''

__author__ = 'Xiang Xue'
__version__ = '1.0'

import os
import sys
import getopt
from colorama import  init, Fore, Back, Style

init(autoreset=True)
class Colored(object):
 
    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.RED + s + Fore.RESET
 
    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.GREEN + s + Fore.RESET
 
    #  前景色:黄色  背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET
 
    #  前景色:蓝色  背景色:默认
    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET
 
    #  前景色:洋红色  背景色:默认
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET
 
    #  前景色:青色  背景色:默认
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET
 
    #  前景色:白色  背景色:默认
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET
 
    #  前景色:黑色  背景色:默认
    def black(self, s):
        return Fore.BLACK
 
    #  前景色:白色  背景色:绿色
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET

    #  前景色:黄色  背景色:白色
    def yellow_white(self, s):
        return Fore.YELLOW + Back.WHITE + s + Fore.RESET + Back.RESET


color = Colored()
# print color.red('I am red!')
# print color.green('I am gree!')
# print color.white_green('I am white green!')

def para_chk():
    # color = Colored()
    if (len(sys.argv) == 2):
        pass    
    else:
        print color.yellow("========================================================")
        print color.yellow(" Warnning: Please input 2 arguments!")
        print color.yellow(" Usage: Python xxx.py work_dir")
        print color.yellow(" e.g.: Python batch_rename_files.py E:\\\\test")
        print color.yellow("========================================================")
        exit()


opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v',['help','filename=','version'])
for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
        print("[*] Help info")
        exit()
    if opt_name in ('-v','--version'):
        print("[*] Version is 0.01 ")
        exit()
    if opt_name in ('-f','--filename'):
        fileName = opt_value
        print("[*] Filename is ",fileName)
        # do something
        exit()


def batch_rename_add_kw(work_dir, kw1, kw2):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new suffix
    '''
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file name
        new_filename = kw1 + os.path.splitext(filename)[0] + kw2 + '.py'
        # Write the files
        os.rename(
          os.path.join(work_dir, filename),
          os.path.join(work_dir, new_filename)
        )

def batch_rename_rm_kw(work_dir, kw1, kw2):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new suffix
    '''
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file name
        fname_without_suffix = os.path.splitext(filename)[0]
        new_filename = fname_without_suffix[int(kw1):-int(kw2)] + '.py'
        # Write the files
        os.rename(
          os.path.join(work_dir, filename),
          os.path.join(work_dir, new_filename)
        )



def main():
    '''
    This will be called if the script is directly envoked.
    '''
    print "Hi,please choose 'A' for add strings, 'D' for delete strings!"

    # Set the variable work_dir with the first argument passed
    work_dir = sys.argv[1]

    user_input = raw_input()
    if user_input == 'A':
        kw1 = raw_input("please input second argument kw1:")
        kw2 = raw_input("please input third argument kw2:")
        batch_rename_add_kw(work_dir, kw1, kw2)
    elif user_input == 'D':
        kw1 = raw_input("please input second argument kw1:")
        kw2 = raw_input("please input third argument kw2:")
        batch_rename_rm_kw(work_dir, kw1, kw2)
    else:
        print color.red("Error,Invalid input!")

    # Set the variable old_ext with the second argument passed
    # kw1 = sys.argv[2]
    # Set the variable new_ext with the third argument passed
    # kw2 = sys.argv[3]


if __name__ == '__main__':
    para_chk()
    main()

