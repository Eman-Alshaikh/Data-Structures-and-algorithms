from re import S
from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.s_q_animal_shelter import AnimalShelter, Cat, Dog


def test_enq_cat():
    a=AnimalShelter()
    seami=Cat('seami')
    a.enqueue(seami)
    assert a.frontcat.name=='seami'


def test_enq_dog():
    a=AnimalShelter()
    rubii=Dog('rubii')
    a.enqueue(rubii)
    assert a.frontdog.name=='rubii'


def test_deq_cat():
    a=AnimalShelter()
    seami,lulu=Cat('seami'),Cat('lulu')
    a.enqueue(seami)

    a.enqueue(lulu)
    a.dequeue('cat')
    assert a.frontcat.name=='lulu'


def test_deq_dog():
    a=AnimalShelter()
    dodo,fofo=Dog('dodo'),Dog('fofo')
    a.enqueue(fofo)

    a.enqueue(dodo)
    a.dequeue('dog')
    assert a.frontdog.name=='dodo'

def test_enq_dog_cat():
    a=AnimalShelter()
    lulu=Cat('lulu')
    fofo=Dog('fofo')
    a.enqueue(fofo)
    a.enqueue(lulu)
    assert a.frontdog.name=='fofo'
    assert a.frontcat.name=='lulu'
    




    



