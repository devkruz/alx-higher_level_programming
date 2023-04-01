#!/usr/bin/python3
import os, sys

current_path = os.path.dirname(os.path.abspath(__file__)) 
parent_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(parent_path)

say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")

say_my_name(12, "White")
