import sys

from bouncy import Bouncy

def main(argv):
    """ main function.
    
    Keyword arguments:
        :param argv: -- argv
    """
    try:
        print (Bouncy.least_number_bouncy_by_percentage(argv[0]))
    except IndexError as error:
        print ("Usage: python zina.py <percentage>")
    except Exception as error:
        print ("Error: " + error.args[0])

#run on bash or terminal
if __name__ == "__main__":
    main(sys.argv[1:])