from django.contrib import admin
from data.model import Level,Student,Speciality,Lecturer,Room,Course,courseOffer
from data.model import admin as adm

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Level)
admin.site.register(courseOffer)
admin.site.register(Course)
admin.site.register(Room)
admin.site.register(Speciality)
admin.site.register(adm)

