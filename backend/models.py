from django.db import models

# Create your models here.
class User(models.Model):
    #userType = models.CharField(max_length = 20, null=True)
    email = models.CharField(max_length = 60)
    password = models.CharField(max_length = 12)

    def __str__(self):
        return self.email + " " + self.password

class Pet(models.Model):
    owner = models.ForeignKey(User, to_field = "id", on_delete=models.CASCADE, default=User.objects.first().pk)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, blank=True, null=True)
    insurance = models.CharField(max_length=100, blank=True, null=True)
    vaccineStatus = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)

    def __str__(self):
        return "name: " + self.name + " type: " + self.type

class Vet(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="nmutlu17@ku.edu.tr")
    password = models.CharField(max_length=100, default="test")
    #patient = models.ForeignKey(Pet, to_field="id", max_length=100)


    def __str__(self):
        return self.name

class Claim(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE, default = User.objects.first().pk)
    pet = models.ForeignKey(Pet, to_field="id", on_delete=models.SET_NULL, blank=True, null=True)
    veterinary = models.ForeignKey(Vet, to_field="id", on_delete=models.SET_NULL, blank = True, null=True)
    pdf = models.FileField(upload_to='files', blank = True, null = True)
    status = models.CharField(max_length=50)
    amount = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Vaccination(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Date of Vaccination')

    def __str__(self):
        return self.name + " " + str(self.date)

class VaccinationCard(models.Model):
    #patient = models.ForeignKey(Pet, to_field="id", on_delete=models.CASCADE, default=Pet.objects.first().pk)
    vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE, default=Vaccination.objects.first().pk)

    def __str__(self):
        return self.id

class Company(models.Model):
    user = models.ForeignKey(User, to_field = "id", on_delete=models.CASCADE, default = User.objects.first().pk)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comments(models.Model):
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, to_field="id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="id")
    comment = models.CharField(max_length=256, null=True)
    star =  models.IntegerField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return str(self.vet) + str(self.user) + self.comment
