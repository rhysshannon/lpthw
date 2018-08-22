class Song(object):
#ok so you just do this because but the two. __init__ is a key thing here. then the two attributes:

# self  
    def __init__(self,lyrics):
        self.lyrics = lyrics
#self used again as the variable. 
    def sing_me_a_song(self):
        #this says for each line in the song print
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you", 
                    "I dont want to get sued", 
                    "So ill stop right there"])

bulls_on_parade = Song(['They rally around the family',
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
# 


class Video(object):

    def __init__(self,movies):
        self.movies = movies
    
    def favourite_movies(self):
        for movie in self.movies:
            print(movie)

action_movie = Video(["Big truble in little china,",
                        "Die Hard",
                        "Hudson Hawk"])

action_movie.favourite_movies()


class Stars(object):
    
    def __init__(self,actors):
        self.actors = actors
    
    def list_of_actors(self):
        for actor in self.actors:
            print(actor)
    
    def count_of_actors(self):
        for actor in self.actors:
            if actor == 'roger moore':
                print("007 Was Ere")
            
            else:
                pass



male_actors = Stars(["Gregory Peck", 
                    "roger moore", 
                    "Bruce Willis"])

female_actors = Stars(["Jodie Forster"])

male_actors.list_of_actors()

female_actors.list_of_actors()

male_actors.count_of_actors()

mystuff = {'apple': "tiger blood"}

print(mystuff['apple'])

class Employees(object):
    def __init__(self, fName, lName):
        self.fname = fName
        self.lname = lName

    
first_name_basis = Stars(["John Vera",
                            "Jim Gutierrez"]
                            )

first_name_basis.list_of_actors()
