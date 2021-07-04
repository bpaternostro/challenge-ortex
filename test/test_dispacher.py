# TODO UNIT TEST
import pytest

from src.core import dispacher as dispa_o

def test_get_exchanges_return_value():
    dispa = dispa_o.Dispacher()
    exchanges = dispa.get_exchanges()
    assert isinstance(exchanges,list)

def test_get_top_exchanges_return_value():
    dispa = dispa_o.Dispacher()
    exchanges = dispa.get_top_exchange()
    assert isinstance(exchanges,tuple)

def test_get_highest_combined_value_eur_return_value():
    dispa = dispa_o.Dispacher()
    highest = dispa.get_highest_combined_value_eur()    
    assert isinstance(highest,tuple)
