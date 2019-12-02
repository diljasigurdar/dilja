class Sentence():
    def __init__(self, sentence=''):
        self.sentence = sentence
    
    def get_first_word(self):
        return self.sentence.split()[0]

    def get_all_words(self):
        return self.sentence.split()
        

    def replace(self, index=0, new_word=''):
        try:
            sentence_list = self.sentence.split()
            sentence_list[index] = new_word
            self.sentence = " ".join(sentence_list)
        except IndexError:
            return None

sent = Sentence('This is a test')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(10, "must")
print(sent.get_all_words())



'''
Design a class called Sentence that has a constructor that takes a string, 
representing the sentence, as input.  The class should have the following methods:

get_first_word(): returns the first word as a string
get_all_words(): returns all words in a list.
replace(index, new_word): Changes a word at a particular index to "new_word".  
For example, if sentence is "I'm going back", then replace(2, "home") results in "I'm going home".  
If the index is not valid, the method does not do anything.'''