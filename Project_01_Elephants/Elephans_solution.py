"""
Background: 

a program that:
- reads the weights of all zoo elephants and the current and target order of the elephants in a 
row from the standard input,
- determine such a way of rearranging elephants, which leads from the initial to the target order and minimizes 
the sum of efforts related to all the changes of elephant positions,
- write the sum of the values of these efforts to the standard output.

EXAMPLE:
input
    6
    2400 2000 1200 2400 1600 4000
    1 4 5 3 6 2
    5 3 2 4 6 1

output
    11200
"""
class Elephants:
    def __init__(self):
        """ The Elephants class is initialized """
        pass
    
    #1 read data from User
    def read_data_n(self):
        """
        This method loads: the number of elephants in the "Bajtockim Zoo" - n (2 <=n <=1 000 000 )
        I line - User input - stores the variable in the <int>
        :return: nothing
        input '6' -->  6
        """
        self.n_amouth_elephans_in_ZOO = int(input()) 
        

    def read_data_elephans_weight(self):
        """
        This method loads: the masses of individual elephants [kg] (100 <=mi <=6500 for 1 <=i<=n)
        II line - User input - stores the variables <int> in the list 
        :return: nothing
        input "2400 2000 1200 2400 1600 4000" --> [2400, 2000, 1200, 2400, 1600, 4000]
        """
        m_weight_of_elephants = input()
        tab_weights = m_weight_of_elephants.split()
        self.elephants_in_kilograms = list(map(int, tab_weights))

    def read_data_a1_employee(self):
        """
        This method loads: the order of elephant placement by employees - a1 (1 <= ai <= n)
        III line - User input - stores the variables <int> in the list
        :return: nothing
        input "1 4 5 3 6 2" --> [1, 4, 5, 3, 6, 2]
        """
        a1_employee_order = input()
        a1_level0 = a1_employee_order.split()
        self.a1 = list(map(int, a1_level0))

    def read_data_b1_boss(self):
        """
        This method loads: the order of elephant placement by dyrector - b1 (1 <= bi <= n)
        IV line - User input - stores the variables <int> in the list
        :return: nothing
        input "5 3 2 4 6 1" --> [5, 3, 2, 4, 6, 1]
        """
        b1_boss_order = input()
        b1_levelFinall = b1_boss_order.split()
        self.b1 = list(map(int, b1_levelFinall))

    def read_data(self):
        """
        This method stores together 4 attributes from the User
        :return: nothing 
        """
        self.read_data_n()
        self.read_data_elephans_weight()
        self.read_data_a1_employee()
        self.read_data_b1_boss()

    
    # 2 - count the cycles
    def create_dict_KEY_valueb1_and_VALUE_indexb1(self,b1):
        """
        This method changes the list b1 to a dictionary - where:
            dictionary key = value b1,
            dictionary value = index_b1

        :param b1: list with integer - list of elephants set by the Director
        :return: dictionary --> {5: 0, 3: 1, 2: 2, 4: 3, 6: 4, 1: 5}
        :purpose: change O(n2)-->O(n) - for method "calculate_chose_method1_or_method2"
        """
        dict_b1 = {}
        for x in range(0, len(b1)):
            dict_b1[b1[x]] = x
        self.dict_b1=dict_b1
        return dict_b1
    
    # attention ! method dosn't use in this code
    def create_dict_KEY_valueb1_and_VALUE_indexb1_methodComprehension(self,b1):
        # alternative way to method "create_dict_KEY_valueb1_and_VALUE_indexb1"
        d = {b1[x]: x for x in range(0, len(b1))}
        return d

    def create_cycles(self, a1,b1):
        """
        This method creates cycles
        :param a1: list with integer - list of elephants arranged by employees
        :param b1: list with integer - list of elephants set by the Director
        :return: list (whole) with lists (single_cycles)  --> whole_cycle=[[1, 2, 5], [3, 4], [6]]; single_cycle=[1, 2, 5] or [3,4] or [6]
        """
        # table initialization - all values False
        good_location = [False for i in range(len(a1))] #=[False for i in range(len(b1))]
        
        whole_cycle = []
      
        dict_b1=self.create_dict_KEY_valueb1_and_VALUE_indexb1(b1) # OR dict_b1 = {b1[x]: x for x in range(0, len(b1))}
        
        for index in range(0, len(a1)):
            if not good_location[index]:
                # wrong standing an elephant
                value = a1[index]
                single_cycle = [value]  # table initialization --> single_cycle=[1]
                good_location[index] = True
                index_value=dict_b1[value]
                while (index_value != index):
                    value_mapping = a1[index_value]
                    single_cycle.append(value_mapping)
                    good_location[index_value] = True
                    index_value=dict_b1[value_mapping]
                whole_cycle += [single_cycle]

        self.whole_cycle=whole_cycle
        return whole_cycle


    # 3- select a method and return the result
    def sum_mass_elephants_one_cycle(self, single_cycle, elephants_in_kilograms):
        """
        This method return common weight of all elephants from a single cycle in [kg]
        :param single_cycle: result method "create_cycles"
        :param elephants_in_kilograms:  (II line - User input + an artificial zero at the beginning)
        :return: common weight <int> -   EXAMPLE : whole_cycle=[[[3, 4]], elephants_in_kilograms=[0, 2400, 2000, 1200, 2400, 1600, 4000])--> 3600
        """
        mass_all_elephants_in_1_cycle=0
        for single_elephant in single_cycle:
            weight_single_elephant = elephants_in_kilograms[single_elephant]
            mass_all_elephants_in_1_cycle += weight_single_elephant

        return mass_all_elephants_in_1_cycle

    def calculate_chose_method1_or_method2(self, whole_cycle, elephants_in_kilograms):
        """
        This method, for each single cycle (single_tab_cycle), 
        calculates the conversion costs (cost_c), using two methods for this purpose (method1_single_cycle and method2_single_cycle). 
        Next chooses the method, that gives the smaller result (less effort to move the elephants).
        And finally, it is added to the final result, which represents the total cost of all adjustments (result). 

        :param whole_cycle: result method "create_cycles"
        :param elephants_in_kilograms:  (II line - User input + an artificial zero at the beginning)
        :return: <int>
        """
        result = 0
        #Attention!!! modifying the input data - added at the beginning 0 - so that you can index the elephants well
        #[2400, 2000, 1200, 2400, 1600, 4000])-->[0,2400, 2000, 1200, 2400, 1600, 4000]
        elephants_in_kilograms.insert(0, 0)  
        
        sum_mass_elephnats_in_single_cycle__sumaC = 0
        tab_mass_elephants_single_cycle = []

        for single_tab_cycle in whole_cycle:

            lenght_of_cycles__C = len(single_tab_cycle)
  
            if lenght_of_cycles__C == 1:
                #the number of the elephant in the table A1 and B1 is the same - conclusion: the elephant does not move - EXAMPLE single_tab_cycle - [6]
                cost_c = 0
            elif lenght_of_cycles__C == 2:
                # we have two elephants. One-time exchange of their seats will ensure that both of them are in a good position - EXAMPLE single_tab_cycle - [3,4]
                # cost, therefore, is the sum of their weights
                cost_c = self.sum_mass_elephants_one_cycle(single_tab_cycle, elephants_in_kilograms)
            else:
                # we have some elephants to organize - EXAMPLE single_tab_cycle [1, 2, 5]
                tab_mass_elephants_single_cycle = []
                for single_elephant in single_tab_cycle:
                    weight_one_elephant_in_single_cycle = elephants_in_kilograms[single_elephant]
                    tab_mass_elephants_single_cycle.append(weight_one_elephant_in_single_cycle)
            
                sum_mass_elephnats_in_single_cycle__sumaC = sum(tab_mass_elephants_single_cycle)
                the_smallest_elephnat_in_single_cycle = min(tab_mass_elephants_single_cycle)
       
                the_smallest_elephant = min(elephants_in_kilograms[1:])

                # formulas (for method1 and method2) in accordance with the guidelines
                method1_single_cycle = sum_mass_elephnats_in_single_cycle__sumaC + (lenght_of_cycles__C-2)*the_smallest_elephnat_in_single_cycle
                method2_single_cycle = sum_mass_elephnats_in_single_cycle__sumaC + the_smallest_elephnat_in_single_cycle + (lenght_of_cycles__C+1)*the_smallest_elephant

                cost_c = min(method1_single_cycle, method2_single_cycle)
         
            result += cost_c
        return result


# LOGIC

if __name__=="__main__":
    # create object class Elephants
    elephants=Elephants()
    # 1- read data
    elephants.read_data()

    # 2 - count the cycles
    elephants.create_cycles(elephants.a1, elephants.b1)

    # 3- select a method and return the result
    program_result = elephants.calculate_chose_method1_or_method2(elephants.whole_cycle, elephants.elephants_in_kilograms)
    print(program_result)