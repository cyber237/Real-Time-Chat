from django.db import models

class admin(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.EmailField()


class Speciality(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=20)


class Lecturer(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)


class Course(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)


class Room(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    state = models.CharField(max_length=10)
    capacity = models.IntegerField()


class Level(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    level = models.IntegerField()
    numOfStud = models.IntegerField()
    timetable = models.CharField(max_length=2200)


class courseOffer(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    timeAllow = models.IntegerField()
    timeLeft = models.IntegerField()


class Student(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
