# batch_file_rename.py
# Created: 14th August 2018

'''
This will batch rename a group of files in a given directory,
once you pass the current and new suffix
'''

__author__ = 'Xiang Xue'
__version__ = '1.0'

import os
import sys
import getopt

def para_chk():
    if (len(sys.argv) == 4):
        pass    
    else:
        print "========================================================"
        print " Error: Please input 3 arguments!"
        print " Usage: Python xxx.py work_dir old_ext new_ext"
        print " e.g.: Python batch_rename_files.py E:\\test .py .txt"
        print "========================================================"
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


def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new suffix
    '''
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1]
        # Start of the logic to check the file suffix, if old_ext = file_ext
        if old_ext == file_ext:
            # Set newfile to be the filename, replaced with the new extension
            newfile = filename.replace(old_ext, new_ext)
            # Write the files
            os.rename(
              os.path.join(work_dir, filename),
              os.path.join(work_dir, newfile)
            )




def main():
    '''
    This will be called if the script is directly envoked.
    '''
    # Set the variable work_dir with the first argument passed
    work_dir = sys.argv[1]
    # Set the variable old_ext with the second argument passed
    old_ext = sys.argv[2]
    # Set the variable new_ext with the third argument passed
    new_ext = sys.argv[3]
    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    para_chk()
    main()

