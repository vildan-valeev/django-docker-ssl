from django.db import models
from django.db.models import Count
from django.db.models import F, ExpressionWrapper, fields
from django.core.paginator import Paginator


class City(models.Model):
    name = models.CharField(max_length=50)


class Person(models.Model):
    name = models.CharField(max_length=50)
    city = models.ManyToManyField(City, related_name="city")


class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


def get_persons(query):
    for person in query:
        print(f'Имя: {person.name}\n'
              f'Город: {person.city.name}')


# # Вывести список людей и городов где они живут?
# person_list_all = Person.objects.all()
# get_persons(person_list_all)
#
# # Вывести всех людей, живущих в городе N
# person_list_city = Person.objects.filter(city__name='Moskow')
# get_persons(person_list_city)
#
# # Вывести 5 городов с наибольшим населением, упорядочив по убыванию.
# big_cities = Person.objects.all().values('city').annotate(total=Count('city')).order_by('-total')[:5]
# for i in big_cities:
#     print(i)
#
# # Реализовать пагинацию с сортировкой по разнице дат
# duration = ExpressionWrapper(F('end_date') - F('start_date'), output_field=fields.DurationField())
# events_with_duration = Event.objects.annotate(duration=duration)
# # ordered = events_with_duration.order_by(-duration) # exception !
# ordered = events_with_duration.order_by(duration)
# # пагинатор
# p = Paginator(events_with_duration, 2)
# print(p.num_pages)
