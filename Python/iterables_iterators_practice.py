class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()


    def __iter__(self):
        return self    #this will return next sentence in the word
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        
        index = self.index
        self.index += 1

        return self.words[index]


def generator_Sentance(sent):
    vals = sent.split()
    for i in vals:
        yield i
    
    

# my_sentence = Sentence('This is a test')

# for word in my_sentence:
#     print(word)

gen_Sen = generator_Sentance('This is a test')

print(gen_Sen)

print(next(gen_Sen))
print(next(gen_Sen))
print(next(gen_Sen))
print(next(gen_Sen))

# for i in gen_Sen:
#     print(i)