from english import get_random_words


players = {}
 
def add_player(id, words_count, complexity):
    players[id] = Player(id, words_count, complexity)
    
    return players[id]

class Player(object):
    def __init__(self, id, words_count, complexity):
        self.id = id
        self.words_count = words_count
        self.complexity = complexity
        self.score = 0
        
    def get_id(self):
        return self.id
    
    def get_new_words(self):
        words = get_random_words(self.words_count, self.complexity)
        self.daily_words = words
        
        response = "Your daily words: \n"
        
        words_string = ",\n".join(words)
        
        return response + words_string
        
        