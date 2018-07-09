"""
Name: Problem_Carry.py
Authors: Christopher Lo - written at University of Pennsylvania, Philadelphia, PA, USA
Contact: chrislo@seas.upenn.edu
Created: November 10, 2016
---------------------------------------------------------------------------------------------------------------------------------------------------------
Problem_Carry: A script designed to generate toy carrying problem datasets.  These are a typical scalable toy problem used in classification and
data mining algorithms such as learning classifier systems.  The 'generate_carry_instance' method will return a single carry instance when called.
The 'generate_carry_data' method will generate a specified number of instances (each having a specified length) and save them to a file.

Lastly, 'generate_complete_carry_data' will attempt to generate all possible unique instances of a carrying problem, where each instance has the
same specified length, assuming there is enough memory to complete the task.  This dataset is also saved to a file.

Copyright (C) 2016 Christopher Lo
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABLILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
---------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import random
import unittest

def generate_carry_data(myfile, num_bits, instances):
    """Generates an even parity dataset with instances instances of num_bits-long boolean strings"""
    print ("Problem_Carry: Generate carrying dataset with " + str(instances) + " instances, each of length " +
           str(2*num_bits) + ".")

    fp=open(myfile,"w")
    #Make File Header
    for i in range(2*num_bits):
        fp.write('n_'+str(i)+"\t")
    fp.write("Class" + "\n") #Carrying condition

    for i in range(instances):
        state_phenotype = generate_carry_instance(num_bits)
        for j in state_phenotype[0]:
            fp.write(str(j)+"\t")
        fp.write(str(state_phenotype[1])+ "\n")

    fp.close()


def generate_carry_instance(num_bits):
    """Generates random boolean string and output"""
    condition1 = []
    for i in range(num_bits):
        condition1.append(str(random.randint(0,1)))
    string1 = ""
    for i in condition1:
        string1 += i

    condition2 = []
    for i in range(num_bits):
        condition2.append(str(random.randint(0, 1)))
    string2 = ""
    for i in condition2:
        string2 += i

    condition = []
    for j in condition1:
        condition.append(str(j))
    for j in condition2:
        condition.append(str(j))

    carry = 1
    sum = bin(int(string1, 2) + int(string2, 2))[2:]
    if len(sum) > num_bits:
        carry = 1
    else:
        carry = 0

    return [condition,carry]

def generate_complete_carry_data(myfile, num_bits):
    """Generates a complete even parity dataset with instances instances of num_bits-long boolean strings"""

    instances = 2**(2*num_bits)

    print("Problem_Complete_Carry: Generate complete carrying dataset with " + str(instances) + " instances, "
          "each of length " + str(2*num_bits) + ".")

    fp = open(myfile, "w")
    # Make File Header
    for i in range(2*num_bits):
        fp.write('n_' + str(i) + "\t")
    fp.write("Class" + "\n")  # Carrying condition

    for i in range(instances):
        condition = str(bin(i))[2:]
        while len(condition) < 2*num_bits:
            condition = "0" + condition

        string1 = condition[:num_bits]
        string2 = condition[num_bits:2*num_bits]
        sum = bin(int(string1, 2) + int(string2, 2))[2:]
        carry = 1
        if len(sum) > num_bits:
            carry = 1
        else:
            carry = 0

        for j in condition:
            fp.write(str(j) + "\t")
        fp.write(str(carry) + "\n")

    fp.close()

# Generate an even parity dataset
generate_carry_data("Carry_Data.txt", 3, 1000)
# Generate a complete even parity dataset
generate_complete_carry_data("Complete_Carry_Data.txt", 3)
# Print a text output
generate_carry_data("Carry_Example.txt", 2, 5)
fp = open('Carry_Example.txt', 'r')
print(fp.read())
fp.close()

#Unit Tests
class Test(unittest.TestCase):
    def test_output(self):
        carry_condition = generate_carry_instance(7)[1]
        self.assertTrue(carry_condition == 0 or carry_condition == 1)

    def test_length(self):
        self.assertTrue(len(generate_carry_instance(7)[0]) == 14)

if __name__ == "__main__":
    unittest.main()