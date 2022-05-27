
from ntpath import join


def repeat_checker(string ,hashtable):

     
    string =string.casefold()
    word_list=string.split('')
    for i,item in enumerate(word_list):
        if not item.isalpha():
            word_list[i]=[character for character in item if character.isalpha()]
            word_list[i]=join(word_list[i])

        if not len(word_list[i]):
            word_list.pop(i)

    print (word_list)


    for word in word_list:
        if hashtable.contains(word):
            return word
        hashtable.add(word,word)