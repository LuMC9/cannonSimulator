from enum import Enum
import sys

class DisplayLists(Enum):
    cannon = 1
    cannonBall = 2

def main():
    
    print(DisplayLists.cannon.value)

if __name__ == '__main__':
    main()