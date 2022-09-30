from django.db import models

class PersonDetailModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    def filesavefun(instance,filename):
        return "/".join([str(instance.owner.name),filename])

    owner = models.ForeignKey(PersonDetailModel, on_delete=models.CASCADE, related_name='owner')
    image = models.ImageField(upload_to=filesavefun)

    def __str__(self):
        return self.owner.name + "Img"