#Github Repo link 
#https://github.com/kwooo5/03230105_BIA101_CAP3.git
#Karma wangmo 
#BBIA
#03230105 

#Reference:
#https://docs.python.org/3/library/os.path.html
#https://docs.python.org/3/tutorial/inputoutput.html

#Solution 
#Solution Score:485617

# Read the input.txtfile
#the os is used to validate the existence of the input file before attempting to read it
import os 

class SumCalculator:
    def __init__(self, input_file):     #Initializing the SumCalculator instance with the input file path and it also calculates the total sum during initialization
        self.input_file = input_file
        self.total_sum = self.calculate_sum()

# reading the input(105).txtfile
    def read_input(self, file_name):
        with open(file_name, "r") as file:
            return file.readlines()

    def calculate_sum(self):
        total_sum = 0
        if os.path.isfile(self.input_file):
            lines = self.read_input(self.input_file)
            for line in lines:
                line = line.strip()
                if line:
                    first_digit, last_digit = self.extract_digits(line)
                    if first_digit is not None and last_digit is not None:
                        number = int(first_digit) * 10 + int(last_digit)
                        total_sum += number
        else:
            print(f"Error: The input file '{self.input_file}' does not exist.")
        return total_sum


    def extract_digits(self, line):   # it extracts the first and last digits from a given line
        digits = ''.join(char for char in line if char.isdigit())
        if len(digits) >= 2:
            return digits[0], digits[-1]
        return None, None
# Solution 
    def print_solution(self):
        print(f"The total sum of the given input file '{self.input_file}' is {self.total_sum}")

# The main function creates a SumCalculator instance and prints the solution
def main():
    input_file = "03230105_BIA101_CAP3/105.txt"  
    calculator = SumCalculator(input_file)
    calculator.print_solution()

if __name__ == "__main__":
    main()