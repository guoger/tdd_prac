#!/bin/python
import sys
import unittest

def grand_total(file_to_read):
    total = 0
    f = open(file_to_read,"r")
    for line in f:
        total += int(line.split(", ")[-1])
        
    return total 

def categorize(ros_file, category_file):
    
    ros = open(ros_file, "r")
    cat = open(category_file, "r")
    cat_dict = {}
    total_dict = {}
    for line in cat:
        (item, category) = line.strip().split(", ")
        if cat_dict.has_key(category):
            cat_dict[category].append(item)
        else:
            cat_dict[category] = [item]
    
    keys = cat_dict.keys()
    for key in keys:
        total_dict[key] = 0

    total_dict["total"] = 0

    for line in ros:
        entry = line.strip().split(", ")
        name = ", ".join(entry[0:-2])
        for key in keys:
            for item in cat_dict[key]:
                if name.find(item) != -1:
                    amount = int(entry[-1])
                    total_dict[key] += amount
                    total_dict["total"] += amount

    return total_dict

class TestGrocery(unittest.TestCase):
    '''
    def test_grand_total(self):
        result = grand_total("grocery.ros")
        what_i_expect = 42
        self.assertEquals(result, what_i_expect)
    '''

    def test_categorize(self):
        result = categorize("grocery.ros", "category")
        what_i_expect = {"wheat and pasta":2, "animalic":2, "dairy":8,
        "sodas":10, "candy":20, "total":42}
        self.assertEquals(result, what_i_expect)



unittest.main()
