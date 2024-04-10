from django.shortcuts import render

from trains.models import Trains

def index(request) :
    allTrains = Trains.objects.all()

    return render(request, "trains/accueil.html", {
        "trains" : allTrains,
    })

def show(request, id_train) :
    myTrain = Trains.objects.get(trainID = id_train, title = "NOMAD")

    return render(request, "trains/show.html", {
        "title" : myTrain.title,
        "release" : myTrain.release,
        "director" : myTrain.producer,
        "precedent" : int(id_train) - 1,
        "suivant" : int(id_train) + 1,
    })

def random(request) :

    return render(request, "trains/random.html", {})