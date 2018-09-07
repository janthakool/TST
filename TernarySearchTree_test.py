from TernarySearchTree import*
import pytest

#this is check verify
""" Verify Testing """
@pytest.mark.parametrize("array,expected",
                         [
                             ("NARESUAN", True),
                             ("ENGINEER", True),
                             ("CPE", True),
                             ("EDUCATION", True),
							 ("EDUCATIONS", True),
							 ("COMPUTER", True),
							 ("SOFTWARE", True),
							 ("HARDWARE", True),
							 ("0112", False),
							 ("HARDWAREs", False),
							 ("SOFTWARES", False),
							 ("CP", False),
							 ("ENGI", False),


                         ])
def test_case(array, expected):
	tree = UsingTST('NARESUAN')
	tree.append("ENGINEER")
	tree.append("CPE")
	tree.append("EDUCATION")
	tree.append("EDUCATIONS")
	tree.append("COMPUTER")
	tree.append("SOFTWARE")
	tree.append("HARDWARE")
	assert tree.search(array) == expected


def test_function1():
	tree = UsingTST('DatasTructure')
	search = tree.search("DatasTructure")
	expected = True
	assert search == expected
	
def test_not_match_on_completeWord():
	tree = UsingTST('DatasTructuress')
	search = tree.search("DatasTructure")
	expected = False
	assert  search == expected


