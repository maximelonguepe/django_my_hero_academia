from django.db import models

# Create your models here.
class Agency(object):
    def __init__(self, id, agencyName, heroes):
        self.id = id
        self.agencyName = agencyName,
        self.heroes = heroes