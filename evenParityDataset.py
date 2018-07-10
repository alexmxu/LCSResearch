"""
Name: Problem_Even_Parity.py
Authors: Christopher Lo - written at University of Pennsylvania, Philadelphia, PA, USA
Contact: chrislo@seas.upenn.edu
Created: November 4, 2016
---------------------------------------------------------------------------------------------------------------------------------------------------------
Problem_Even_Parity: A script designed to generate toy even parity problem datasets.  These are a typical scalable toy problem used in classification
and data mining algorithms such as learning classifier systems.  The 'generate_even_parity_instance' method will return a single even parity instance
when called. The 'generate_even_parity_data' method will generate a specified number of instances (each having a specified length) and save them to a
file.

Lastly, 'generate_complete_even_parity_data' will attempt to generate all possible unique instances of an even parity problem, where each instance
have the same specified length, assuming there is enough memory to complete the task.  This dataset is also saved to a file.  Below we break down
the first 8 multiplexer problems, where the number of address bits determines the total length of the multiplexer binary string.

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

def generate_even_parity_data(myfile, num_bits, instances):
    """Generates an even parity dataset with instances instances of num_bits-long boolean strings"""
    print ("Problem_Even_Parity: Generate even parity dataset with " + str(instances) + " instances, each of length " + str(num_bits) + ".")

    fp=open(myfile,"w")
    #Make File Header
    for i in range(num_bits):
        fp.write('n_'+str(i)+"\t")
    fp.write("Class" + "\n") #Parity

    for i in range(instances):
        state_phenotype = generate_even_parity_instance(num_bits)
        for j in state_phenotype[0]:
            fp.write(str(j)+"\t")
        fp.write(str(state_phenotype[1])+ "\n")

    fp.close()


def generate_even_parity_instance(num_bits):
    """Generates random boolean string and output"""
    condition = []
    for i in range(num_bits):
        condition.append(str(random.randint(0,1)))

    num_ones = 0
    for j in range(num_bits):
        if condition[j] == "1":
            num_ones += 1
    if num_ones % 2 == 0:
        parity = 1
    else:
        parity = 0

    return [condition,parity]

def generate_complete_even_parity_data(myfile, num_bits):
    """Generates a complete even parity dataset with instances instances of num_bits-long boolean strings"""

    instances = 2**num_bits

    print("Problem_Complete_Even_Parity: Generate complete even parity dataset with " + str(instances) + " instances, "
          "each of length " + str(num_bits) + ".")

    fp = open(myfile, "w")
    # Make File Header
    for i in range(num_bits):
        fp.write('n_' + str(i) + "\t")
    fp.write("Class" + "\n")  # Parity

    for i in range(instances):
        condition = str(bin(i))

        condition = condition[2:]

        while len(condition) < num_bits:
            condition = "0" + condition

        num_ones = 0
        for j in range(num_bits):
            if condition[j] == "1":
                num_ones += 1
        if num_ones % 2 == 0:
            parity = 1
        else:
            parity = 0

        for k in condition:
            fp.write(str(k) + "\t")
        fp.write(str(parity) + "\n")

    fp.close()

# Generate an even parity dataset
generate_even_parity_data("Even_Parity_Data.txt", 8, 1000)
# Generate a complete even parity dataset
generate_complete_even_parity_data("Complete_Even_Parity_Data.txt", 5)
# Print a text output
generate_even_parity_data("Even_Parity_Example.txt", 10, 10)
fp = open('Even_Parity_Example.txt', 'r')
print(fp.read())
fp.close()

#Unit Tests
class Test(unittest.TestCase):
    def test_output(self):
        self.assertTrue(generate_even_parity_instance(7)[-1] == 0 or generate_even_parity_instance(7)[-1] == 1)

    def test_length(self):
        self.assertTrue(len(generate_even_parity_instance(7)[0]) == 7)

if __name__ == "__main__":
    unittest.main()