import os
import sys

# Adds "src" to sys.path
# "src" contains a package "selenium"
# Now you can do import with "from selenium.Sub-Package ..."
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "src")))
