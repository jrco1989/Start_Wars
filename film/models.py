from django.db import models


class Film (models.Model):
    films=(('I','La amenaza fantasma'),
          ('II','El ataque de los clones'),
          ('III','La venganza de los Sith'),
          ('IV','Una nueva esperanza'),
          ('V','El Imperio contraataca'),
          ('VI','Return of the Jedi'),
          ('VII','El despertar de la Fuerza'),
          ('VIII','Los últimos Jedi'),
          ('IX','El ascenso de Skywalker'))

    title= models.CharField(max_length=4, choices=films, 
                            blank=False, default='I', 
                            help_text='select a options')
  
    opening_text=models.TextField(max_length=1000, 
                                  help_text="insert the text opening")
    
    director=models.CharField(max_length=50,help_text="Enter the director's name")
    

    def __str__(self):
        return self.title 

class Character (models.Model):
    name_character=models.CharField(max_length=50,
                                    blank=False, 
                                    help_text="Enter the chracter's name")
    actor=models.CharField(max_length=50,
                            blank=True, 
                            help_text="Enter the real name of the chracter")
    performances=models.ManyToManyField(Film, 
                        help_text="select the movies in which the character appears")
    def __str__(self):
        return self.name_character
