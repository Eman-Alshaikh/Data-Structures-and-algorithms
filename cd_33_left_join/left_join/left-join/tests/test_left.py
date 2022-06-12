import pytest
from  left_join.hash import HashTable
from  left_join.left_join_def import left_join_fun


def test_get():
    hash_one=HashTable()    
    hash_one.set('diligent','employed')
    hash_one.set('fond','enamored')      
    hash_one.set('guide','usher')
  
    hash_one.set('outfit','garb')

    hash_one.set('wrath','anger')

    assert hash_one.get('fond')=='enamored'



def test_contains():
    hash_one=HashTable()
    hash_one.set('diligent','employed')
    hash_one.set('fond','enamored')      
    hash_one.set('guide','usher')
  
    hash_one.set('outfit','garb')

    hash_one.set('wrath','anger')

    assert hash_one.contains('fond')== True



def test_left_join():
    hash_one=HashTable()

    hash_one.set('diligent','employed')
    hash_one.set('fond','enamored')      
    hash_one.set('guide','usher')
  
    hash_one.set('outfit','garb')

    hash_one.set('wrath','anger')

    hash_two=HashTable()
    hash_two.set('diligent','idle')

    hash_two.set('fond','averse')
    hash_two.set('guide','follow')
    hash_two.set('flow','jam')

    hash_two.set('wrath','delight')


    assert left_join_fun(hash_one,hash_two)==[['diligent','enamored','idle'],['wrath','anger','diligent'],['guide','usher','follow'],['fond','enamored','averse'],['outfit','garb',None]]


     


