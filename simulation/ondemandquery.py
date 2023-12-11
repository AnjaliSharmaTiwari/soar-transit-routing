"""
This is the module to run the On Demand Query engine
"""

import os

python_global_call = 'python'

# python_global_call = 'python3'
os.system(f'{python_global_call} GTFS_wrapper.py')
os.system(f'{python_global_call} ./builders/build_transfer_file.py')
os.system(f'{python_global_call} ./builders/build_TBTR_dict.py')
os.system(f'{python_global_call} ./builders/build_transfer_patterns.py')
os.system(f'{python_global_call} ./builders/build_CSA.py')

def take_inputs() -> tuple:

    algorithm = int(input(
        "Press 0 to enter SOAR environment \nPress 1 to enter Walking environment\nPress 2 to enter Transfer Patterns environment\n: "))
    variant = 0
    print("***************")
    if algorithm == 0:
        variant = int(input(
            "Press 0 for SOAR \nPress 1 for wSOAR \nPress 2 for One-To-Many wSOAR \n: "))
    elif algorithm == 1:
        variant = int(input("Press 0: SOAR \nPress 1: wSOAR \nPress 2: One-To-Many wSOAR \n: "))
    print("***************")
    return algorithm, variant


def main() -> None:
    """
    Runs the test case depending upon the values of algorithm, variant

    Examples:
        >>> main()

    """

  # main function
  d_time_groups = stop_times_file.groupby("stop_id")
  main()
