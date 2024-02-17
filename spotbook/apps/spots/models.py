from django.contrib.gis.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class SpotFollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class SpotLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey("Spot", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) 

class Spot(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250)
    location = models.PointField(srid=4326)
    description = models.TextField()

    SKATEPARK = 'Skatepark'
    STREET = 'Street'
    DIY = 'D.I.Y'
    SPOTTYPES = [
        (SKATEPARK, ('Skatepark')),
        (STREET, ('Street')),
        (DIY, ('D.I.Y')),
    ]
    spotType = models.CharField(max_length=32, choices=SPOTTYPES)
    
    likes = models.ManyToManyField(User, related_name="spot_user", blank=True, through=SpotLike)
    timestamp = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(User, related_name='following_spots', blank=True)

    '''
    spot_obj = Spot.objects.first()
    spot_obj.followers.all() -> All users follwing this spot
    user.following_spots.all() -> All spots I follow
    '''

    def __str__(self):
        return self.title


class SpotList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class SpotListItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    spotlist = models.ForeignKey(SpotList, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
