import pytest
from aoc.day_08 import Day08
from resources import read_as_string_list, file_exists

local_test = file_exists("test/day08.in")
aoc_input = Day08(read_as_string_list("test/day08.in")) if local_test else None
test_input = Day08(read_as_string_list("test/day08.example"))


def test_solve_1_examples():
    assert test_input.solve1() == 6


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 121


def test_solve_2_examples():
    assert (
        test_input.solve2()
        == """
    # #                                           
# #                                               
 #                                                
 #                                                
                                                  
                                                  """
    )


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert (
        aoc_input.solve2()
        == """
###  #  # ###  #  #  ##  ####  ##  ####  ### #    
#  # #  # #  # #  # #  # #    #  # #      #  #    
#  # #  # #  # #  # #    ###  #  # ###    #  #    
###  #  # ###  #  # #    #    #  # #      #  #    
# #  #  # # #  #  # #  # #    #  # #      #  #    
#  #  ##  #  #  ##   ##  ####  ##  ####  ### #### """
    )
