from cd_31.hash import HashTable


def the_repeated_word(sentence):
   """
    Write a function called repeated word that finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    """

   if type(sentence) is not str:
        return "the input string should be string only"
 

   individuals=HashTable()
   words=sentence.lower().split(' ')
   for word in words : 
       if individuals.get(word) is None:
           individuals.set(word,words)
       
       else:
           return word

   

 