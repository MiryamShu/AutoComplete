# AutoComplete
By google

Storage the data:

In the first we make a Data Structure that will help us in the search:
1. Dictionary - 
    Key = word from the data.
    Valeu = Trie that contains the continuation of the sentences from this word- 
            Inside the leaf is an object with the details of the sentence(file, line, and more).
2. Trie - 
    Contains all the words in the data. 
    
    
The search:
