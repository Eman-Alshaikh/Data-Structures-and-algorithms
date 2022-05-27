# Hashtables
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

The basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value. This is done through what we call a hash. A hash is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value.

Since we are able to hash our key and determine the exact location where our value is stored, we can do a lookup in an O(1) time complexity. This is ideal when quick lookups are required.

## Terminology:
1- Hash - A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the array.

2- Buckets - A bucket is what is contained in each index of the array of the hashtable. Each index is a bucket. An index could potentially contain multiple key/value pairs if a collision occurs.

3- Collisions - A collision is what happens when more than one key gets hashed to the same location of the hashtable.
## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the 5 methods .


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I used a Linked List data structure at each index of the Hash Table to handle the collision senario . 

adding key/value pairs and getting values from the Hash Table is essentially O(1) for the time for the set and get methods . Big O : is always looking for the worst case senarion . here the wirst case would be the length of the Linked List at any given index . if one of the indexes has 3 collisions , the big O for the time will be O(3) . 

## API
<!-- Description of each method publicly available in each of your hashtable -->

the Hash Table has 5 methods : 

1- set(self,key,value): it takes  as Arguments and returns: nothing.  This method should hash the key, and set the key and value pair in the table, handling collisions as needed.Should a given key already exist, replace its value from the value argument given to this method.
  
2-  get (self,key): it takes key as Arguments and Returns the  Value associated  with that key in the table
         
 
3- contains (self,key): it takes key as Arguments and returns: Boolean, indicating if the key exists in the table already.
 
4-keys(self):Returns the  Collection of keys

 
5-hash(self,key): it takes  key as      Arguments and Returns the  Index in the collection for that key
      

         

