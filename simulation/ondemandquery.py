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


def main() -> None:
    """
    Runs the test case depending upon the values of algorithm, variant

    Examples:
        >>> main()

    """

  # main function
  d_time_groups = stop_times_file.groupby("stop_id")
  main()
