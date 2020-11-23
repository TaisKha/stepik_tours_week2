import random

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from stepik_tours_week2.data import tours, departures, title, subtitle, description


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... 404!')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что то сломалось... 500!')


class DepartureView(View):
    def get(self, request, departure_id):
        context = {}
        for i in range(1, 17):
            tours[i]['id'] = i
        relevant_tours_id = list(filter(lambda x: tours[x]['departure'] == departure_id, tours.keys()))
        context['relevant_tours'] = [tours[id] for id in relevant_tours_id]
        context['count'] = len(relevant_tours_id)
        context['min_nights'] = min([tours[id]['nights'] for id in relevant_tours_id])
        context['max_nights'] = max([tours[id]['nights'] for id in relevant_tours_id])
        context['min_price'] = min([tours[id]['price'] for id in relevant_tours_id])
        context['max_price'] = max([tours[id]['price'] for id in relevant_tours_id])
        context['departure_text'] = departures[departure_id]
        context['departures'] = departures

        return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        context = {}
        context['tour'] = tours[id]
        context['printed_stars'] = '★' * int(tours[id]['stars'])
        context['departure_text'] = departures[tours[id]['departure']]
        context['title'] = title
        context['subtitle'] = subtitle
        context['departures'] = departures
        return render(request, 'tour.html', context=context)


class MainView(View):
    def get(self, request):
        random_arr = []
        while len(set(random_arr)) != 6:
            random_arr = [random.randint(1, 16) for _ in range(6)]
        context = {}
        for i in range(1, 17):
            tours[i]['id'] = i
        context['tours'] = [tours[id] for id in random_arr]
        context['title'] = title
        context['subtitle'] = subtitle
        context['description'] = description
        context['departures'] = departures
        return render(request, 'index.html', context=context)
