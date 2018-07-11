import random

def generate_count_ones_data(myfile, num_bits, instances):
    """Generates a count ones dataset with instances instances of num_bits-long boolean strings"""
    print ("Problem_Count_Ones: Generate count ones dataset with " + str(instances) + " instances, each of length " + str(num_bits) + ".")

    fp=open(myfile,"w")
    #Make File Header
    for i in range(num_bits):
        fp.write('n_'+str(i)+"\t")
    fp.write("Class" + "\n") #Parity

    for i in range(instances):
        state_phenotype = generate_count_ones_instance(num_bits)
        for j in state_phenotype[0]:
            fp.write(str(j)+"\t")
        fp.write(str(state_phenotype[1]) + "\n")

    fp.close()


def generate_count_ones_instance(num_bits):
    """Generates random boolean string and output"""
    condition = []
    for i in range(num_bits):
        condition.append(str(random.randint(0,1)))
    num_ones = 0

    for j in range(num_bits):
        if condition[j] == "1":
            num_ones += 1
    if num_ones > int(num_bits/2):
        action = 1
    else:
        action = 0
    return [condition, action]


def generate_complete_count_ones_data(myfile, num_bits):
    """Generates a complete majority on dataset with instances instances of num_bits-long boolean strings"""
    instances = 2**(num_bits)

    print("Problem_Complete_count_ones: Generate complete majority on dataset with " + str(instances) + " instances, "
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
        if num_ones > int(num_bits/2):
            action = 1
        else:
            action = 0

        for k in condition:
            fp.write(str(k) + "\t")
        fp.write(str(action) + "\n")

    fp.close()


# Generate an even parity dataset
generate_count_ones_data("Count_Ones_Data.txt", 8, 1000)
# Generate a complete even parity dataset
generate_complete_count_ones_data("Complete_Count_Ones_Data.txt", 5)
# Print a text output
generate_count_ones_data("Count_Ones_Example.txt", 10, 10)
fp = open('Count_Ones_Example.txt', 'r')
print(fp.read())
fp.close()