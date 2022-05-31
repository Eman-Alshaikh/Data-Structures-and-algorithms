from cd_30.hash import HashTable

def test_set():
    table=HashTable( )
    table.set('eman',26)
    table.set('elyas',24)
    table.set('mohammad',28)

    assert table.bucket[table.hash('eman')].head.value==("eman",26)

def test_key_not_exist():
    table=HashTable( )
    assert table.get('nemer')=='NULL'

def test_handle_collision():
    table=HashTable()
    table.set('leen',"1")
    table.set('neel',"2")
    assert table.bucket[table.hash('leen')].head.value==("leen",'1')
    assert table.bucket[table.hash('neel')].head.next.value==("neel",'2')

def test_hash_keys():
    table=HashTable()
    table.keys()
    print(table)
    assert['eman','elyas','mohammad']


def test_get():
    table=HashTable()
    table.set('eman',26)
    assert table.get('eman')==26

def test_get_none():
    table=HashTable()
    assert table.get('key')=='NULL'



 

  

