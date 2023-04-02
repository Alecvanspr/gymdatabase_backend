from django.db import models
from django.contrib.auth.models import User

class MuscleGroup(models.Model):
    name= models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    parentGroup = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.name)

class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    muscle_groups = models.ManyToManyField(MuscleGroup, null=True, blank=True)
    exercises = models.ManyToManyField("Exercise", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.name)

class Location(models.Model):
    organisation = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10, default='0')
    place = models.CharField(max_length=100)
    zipcode= models.CharField(max_length=6)
    country = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.street)+' - ' +str(self.organisation)

class Session(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    preworkout = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    training = models.ForeignKey(Training,on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.date)

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Exercise(models.Model):
    muscle_group = models.ManyToManyField(MuscleGroup, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=300, null=True, blank=True)
    help_video = models.CharField(max_length=300, null=True, blank=True)
    cardio = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.name) +" - "+str(self.equipment.name)

class Set(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    exercise = models.ForeignKey(Exercise, on_delete= models.CASCADE,related_name="sets")
    set_count = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device = models.CharField(default="Auto",max_length=250)

    def __str__(self):
        return str(self.session.date)+'-'+str(self.exercise.name)+'('+str(self.set_count)+')' 

class CardioSet(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    time = models.TimeField()
    distance = models.FloatField()
    resistanceNiveau = models.IntegerField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device = models.CharField(default="Auto",max_length=250)

    def __str__(self):
        return str(self.session.date)+'-'+str(self.exercise.name)+'('+str(self.time)+')'

class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)    
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now=True, null=True)

class PersonalInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=100)
    birthdate = models.DateField()
    height = models.FloatField()
    createad_at = models.DateTimeField(auto_now=True, null=True)

    def get_weight(self):
        return Weight.objects.filter(user=self.user).last()

