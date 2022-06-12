from  cd_31.repeat_word import HashTable,the_repeated_word
 
import pytest


@pytest.mark.parametrize(
    "test_string,hashtable,expected",
    [

        ('Once upon a time, there was a brave princess who...',HashTable(),'a'),
        ('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..',HashTable(),'it'),
        ('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York.',HashTable(),'summer')


    ]


)
def test_1(test_string,hashtable,expected):
    actual=the_repeated_word(test_string,hashtable)
    assert actual==expected
 
    
     