class Team:

    def __init__(self):
        """ Asks for the user input for a noun and stores the noun in
        the instance variable self.word.  Remember a noun is a person,
        place, or thing. """
        self.word = raw_input('Enter Name or Place: ')
        

    def reverse_input(self):          
        self.word = self.word[::-1]         
        pass
    
    def print_in_sentence(self):
        print 'Today I dreamt of',  self.word, 'while walking on the beach.'
      # TODO by person 2
        pass

t = Team()
t.reverse_input()
t.print_in_sentence()
