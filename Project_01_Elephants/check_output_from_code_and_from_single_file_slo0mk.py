"""
purpose: to compare results from .out files with results from code from "Elephans_solution.py" file

steps:
1. entry to the "task_B /" folder - where the .in file and the corresponding .out file are located

2. loading the .in # file "slo0mk.in"
3. load corresponding .out file # "slo0mk.out"

4. checking the correctness of the written code - by comparing 2 results:
- resultatu from the "Elephans_solution.py" file - result_from_code
- with the result from the "slo0mk.out" file  - result_from_file_with_answer
"""

from Elephans_solution import Elephants  # import klasy ze wszytskimi metodami
import Elephans_solution  # import pliku
import mock

with open("zadanie_B/slo0mk.in", "r") as file:
    first_line=file.readline()
    second_line = file.readline()
    third_line = file.readline()
    fourth_line = file.readline()
    file.close()

def test_read_data():
    line1 = first_line
    line2 = second_line
    line3 = third_line
    line4 = fourth_line
   
    with mock.patch('builtins.input', return_value=line1):
        elephants.read_data_n()

    with mock.patch('builtins.input', return_value=line2):
        elephants.read_data_elephans_weight()
 
    with mock.patch('builtins.input', return_value=line3):
        elephants.read_data_a1_employee()

    with mock.patch('builtins.input', return_value=line4):
        elephants.read_data_b1_boss()


# getting the result from the slo0mk.out file
with open('zadanie_B/slo0mk.out', "r") as file:
    result_from_file_with_answer = file.readline()
    
  
    
if __name__ == "__main__":
    # create object class Elephants
    elephants = Elephants()

    # loading data from our function, not Elephants!!
    test_read_data() 
    """
    print(elephants.n_amouth_elephans_in_ZOO)
    print(elephants.elephants_in_kilograms)
    print(elephants.a1)
    print(elephants.b1)
    """
    # 2- count the cycles
    elephants.create_cycles(elephants.a1, elephants.b1)

    # 3- select a method and return the result
    resultat_from_code = elephants.calculate_chose_method1_or_method2(
        elephants.whole_cycle, elephants.elephants_in_kilograms)
    print("nazwa pliku z wynikiem: ", "slo0mk.out")
    print("Resultat z pliku 'slo0mk.out': ", result_from_file_with_answer)
    print("Resultat z pliku 'Elephans_solution.py': ", resultat_from_code)
    print("Porownanie wynikow z pliku i z kodu: ", resultat_from_code == int(result_from_file_with_answer))


