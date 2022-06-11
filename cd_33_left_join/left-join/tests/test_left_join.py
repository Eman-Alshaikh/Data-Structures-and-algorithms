import pytest
from  left_join.demo import HashTable as HT
from left_join.demo import leftJoin

@pytest.fixture
def hash_table_1_syn():
    hash=HT(5)
    hash.set('fond', 'enamored')
    hash.set('wrath', 'anger')
    hash.set('diligent', 'employed')
    return hash

@pytest.fixture
def hash_table_1_ant():
    hash=HT(5)
    hash.set('fond', 'averse')
    hash.set('wrath', 'delight')
    hash.set('diligent', 'idle')
    return hash

@pytest.fixture
def hash_table_2_syn():
    hash=HT(6)
    hash.set('guide', 'usher')
    hash.set('wrath', 'anger')
    hash.set('diligent', 'employed')
    hash.set('outfit', 'garb')

    return hash

@pytest.fixture
def hash_table_2_ant():
    hash=HT(6)
    hash.set('fond', 'averse')
    hash.set('wrath', 'delight')

    hash.set('guide', 'follow')
    hash.set('flow', 'jam')

    return hash

def test_left_join_two(hash_table_2_syn,hash_table_2_ant):
    assert leftJoin(hash_table_2_syn,hash_table_2_ant)== [
  
   ['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'NULL'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]

def test_left_join_two(hash_table_2_syn,hash_table_2_ant):
    assert leftJoin(hash_table_2_syn,hash_table_2_ant)== [
  
   ['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'NULL'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]

def test_left_join_two(hash_table_2_syn,hash_table_2_ant):
    assert leftJoin(hash_table_2_syn,hash_table_2_ant)== [
  
   ['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'NULL'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]

def test_left_join_two(hash_table_2_syn,hash_table_2_ant):
    assert leftJoin(hash_table_2_syn,hash_table_2_ant)== [
  
   ['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'NULL'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]
"""
"""
    

