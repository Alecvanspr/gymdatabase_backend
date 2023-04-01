from django.contrib import admin
from .models import Session, Set, Exercise , Location, MuscleGroup, Trainday, Equipment

# Customized filters
class SelectMuscleGroup(admin.SimpleListFilter):
    title = ('Select muscle group')
    parameter_name = 'name'

    def lookups(self, request, model_admin):
        return (
            ('Chest', ('Chest')),
            ('Back', ('Back')),
            ('Arms', ('Arms')),
            ('Legs',('Legs')),
            ('Abdominals', ('Abdominals')),
            ('Shoulders', ('Shoulders')),
        )
    
    def queryset(self,request, queryset):
        if(self.value()):
            if(queryset.model.__name__=="MuscleGroup"):
                return queryset.filter(parentGroup__name=self.value())
            elif(queryset.model.__name__=="Exercise"):
                return queryset.filter(muscle_group__name=self.value())
        return queryset.order_by('name')
    
class SelectGroupTypes(admin.SimpleListFilter):
    title = ("Select muscle type")
    parameter_name = "muscle group type"

    def lookups(self,request, model_admin):
        return (
            ("Major",("Major muscle groups")),
            ("Minor", ("Minor muscle groups"))
        )
    
    def queryset(self,request,queryset):
        if(self.value()):
            return queryset.filter(type=self.value())
        return queryset

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    ordering = ['-date']
    pass

class SetAdmin(admin.ModelAdmin):
    search_fields = ('session__date',)
    pass

class ExerciseAdmin(admin.ModelAdmin):
    list_filter = (SelectMuscleGroup,)
    search_fields = ['MuscleGroup']
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class MuscleGroupAdmin(admin.ModelAdmin):
    list_filter = [SelectMuscleGroup,SelectGroupTypes]
    pass

class TrainDayAdmin(admin.ModelAdmin):
    pass

class EquipmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Trainday, TrainDayAdmin)
admin.site.register(MuscleGroup,MuscleGroupAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(Equipment,EquipmentAdmin)



