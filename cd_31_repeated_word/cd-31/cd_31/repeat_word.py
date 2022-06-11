from cd_31.linked import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        # None can be replaced with LinkedList() at higher initial setup cost
        self._buckets = size * [None]

    def _hash(self, key):
        sum = 0
        for character in key:
            sum += ord(character)

        primed = sum * 599
        index = primed % self._size
        return index

    def add(self, key, value):
        hashed_key_index = self._hash(key)
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].append((key, value))

    def get(self, key):
        requested_key = self._hash(key)
        if self._buckets[requested_key]:
            current = self._buckets[requested_key].head
            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next
        else:
            return None

    def contains(self, key):
        requested_key = self._hash(key)
        if self._buckets[requested_key]:
            current = self._buckets[requested_key].head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        else:
            return False


    
    





def the_repeated_word(string,hashtable):


   """
    Write a function called repeated word that finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    """
   string=string.casefold()

   word_list=string.split(' ')
   for i,item in enumerate(word_list):
     if not item.isalpha():
        word_list[i]=[
            char for char in item if char.isalpha()

        ]

     if not len(word_list[i]):
        word_list.pop(i)


   for word in word_list:
        if hashtable.contains(word):
            return word
        hashtable.set(word,word)
   return None



    