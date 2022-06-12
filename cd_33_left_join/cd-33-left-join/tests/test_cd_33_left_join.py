import pytest
from cd_33_left_join.hash import  Hashtable
from cd_33_left_join.left import left_join


def test_get():
    hash_one=Hashtable()    
    hash_one.set('fond','enamored')
    hash_one.set('wrath', 'anger')       
    hash_one.set('diligent', 'employed')
  
    hash_one.set('outfit','garb')

    hash_one.set('guide', 'usher')

    assert hash_one.get('fond')=='enamored'



def test_contains():
    hash_one=Hashtable()
    hash_one.set('diligent','employed')
    hash_one.set('fond','enamored')      
    hash_one.set('guide','usher')
  
    hash_one.set('outfit','garb')

    hash_one.set('wrath','anger')

    assert hash_one.contains('fond')== True


 



 



 