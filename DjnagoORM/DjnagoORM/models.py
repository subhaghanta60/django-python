from django.db import models

import uuid
from django.contrib.auth.models import User


class YoutubeVideo(models.Model):
    video = models.Filefeild(upload_to ="youtube")


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_keys=True,editable=false)
    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract= True

# [abstract = True] => BaseModel Will not migrate in DB .It can used Other Model To automatically add It's Row Like uid,Created_at

class Colors(BaseModel):
    color_code = models.charField(max_length=100)



class People(BaseModel):
    name = models.CharField(max_length=100)
    about = models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    colors=models.ManytoManyFields(colors)


class PeopleAddress(BaseModel):
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="address")
    address= models.TextField()





