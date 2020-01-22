from django.db import models


class Film (models.Model):
    """films=(('La amenaza fantasma','La amenaza fantasma'),
          ('II','El ataque de los clones'),
          ('III','La venganza de los Sith'),
          ('IV','Una nueva esperanza'),
          ('V','El Imperio contraataca'),
          ('VI','Return of the Jedi'),
          ('VII','El despertar de la Fuerza'),
          ('VIII','Los últimos Jedi'),
          ('IX','El ascenso de Skywalker'))"""

    title= models.CharField(max_length=40, 
                            help_text='select a options')
  
    opening_text=models.TextField(max_length=1000, 
                                  help_text="insert the text opening")
    
    director=models.CharField(max_length=50,help_text="Enter the director's name")

    #personage=models.ManyToManyField('Personage', blank=True, help_text='select the personages')
    

    def __str__(self):
        return self.title 

class Personage (models.Model):
    name_personage=models.CharField(max_length=50,
                                    blank=False, 
                                    help_text="Enter the personage's name")
    actor=models.CharField(max_length=50,
                            blank=True, 
                            help_text="Enter the real name of the personage")
    performances=models.ManyToManyField(Film, 
                        help_text="select the movies in which the personage appears")
    def __str__(self):
        return self.name_personage
