from hash_table.hash import HashTable


def test_add():
    table=HashTable( )
    table.set('eman',"26")
    assert table.map[table.hash('eman')].head.value==("eman",'26')

def test_key_not_exist():
    table=HashTable( )
    assert table.get('nemer')=='NULL'


def test_handle_collision():
    table=HashTable()
    table.set('leen',"1")
    table.set('neel',"2")
    assert table.map[table.hash('leen')].head.value==("leen",'1')
    assert table.map[table.hash('neel')].head.next.value==("neel",'2')




 
  