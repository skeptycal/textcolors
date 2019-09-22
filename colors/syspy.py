
import os
import pygments.

def basename(s: str) -> str:
    """
    get only basename from full path
    # TODO translate to pathlib
    """
    return os.path.basename(s)

def pprint_globals():
    print()
    print ("Globals: ")
    print ("*"*40)
    for s in globals():
        print("{:<15.15} : {:<64.64}".format(s,str(globals().get(s))))

if __name__ == "__main__":
    pprint_globals()
    print()
    print('basename: ', basename(__file__))
