class Team:

    def __init__(self):
        """ Asks for the user input for a noun and stores the noun in
        the instance variable self.word.  Remember a noun is a person,
        place, or thing. """
        self.word = raw_input('Enter Name or Place: ')
        

    def reverse_input(self):
        """ Changes self.word to its reverse.  For example if
        self.word is 'apples', then it becomes 'selppa'."""
        self.word [::-1]
#        reverseWord = ''
#        for i in range(len(self.word)-1,-1,-1):
#            reverseWord += self.word
#        self.word = reverseWord          
#        return self.word             
#        
    
    def print_in_sentence(self):
       print 'Today I dreamt of',  self.word, 'while walking on the beach.'
       """ Insert self.word in the sentence 'Today I dreamt of
        <self.word> while walking on the beach.' replacing <self.word>
        for the noun that was chosen during class construction. """
	  # TODO by person 2
       

t = Team()
t.reverse_input()
t.print_in_sentence()
