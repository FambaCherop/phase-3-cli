# main.py
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from recipes.cli import main

if __name__ == "__main__":
    main()
