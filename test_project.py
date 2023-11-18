import pytest
from project import convert_RGB_to_12_scale
from project import modify_array
from project import print_ASCII_to_terminal


def test_convert_RGB_to_12_scale():
    assert convert_RGB_to_12_scale(0) == 1
    assert convert_RGB_to_12_scale(15) == 1
    assert convert_RGB_to_12_scale(19) == 1
    assert convert_RGB_to_12_scale(20) == 2
    assert convert_RGB_to_12_scale(255) == 12
    assert convert_RGB_to_12_scale(255) == 12
    assert convert_RGB_to_12_scale(-5) == -1
    assert convert_RGB_to_12_scale(256) == -1
    assert convert_RGB_to_12_scale(300) == -1

def test_modify_array():
    grayscale_array = [[100, 200, 255], [0, 20, 40]]
    assert modify_array(grayscale_array) == [[6, 11, 12], [1, 2, 3]]
    grayscale_array = [[0, 0, 0], [0, 0, 256]]
    assert modify_array(grayscale_array) == [[1, 1, 1], [1, 1, -1]]

    
def test_print_ASCII_to_terminal(capfd):
    grayscale_array = [[6, 11, 12], [1, 2, 3]]
    print_ASCII_to_terminal(grayscale_array)
    out, err = capfd.readouterr()
    assert out == ";$@\n.,-\n"
