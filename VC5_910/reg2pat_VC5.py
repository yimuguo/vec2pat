import os
import sys
import glob

# Read Summary File


def find_summary(search_path):
    os.chdir(search_path)
    try:
        for file in glob.glob("*summary*.txt"):
            filename = file
            summary_file = open(filename, 'r')
            break
    except (RuntimeError, TypeError, NameError):
        sys.exit('No Summary Txt File Present')
    finally:
        return summary_file

vc5_file = find_summary('.\\code\\')
