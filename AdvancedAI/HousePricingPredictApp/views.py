from django.shortcuts import render
from .train import predict_price


# Create your views here.
def home(request):
    return render(request, "home.html")


def predict(request):
    return render(request, "predict.html")


def result(request):
    n1, n2, n3, n4, n5 = (
        request.GET["n1"],
        request.GET["n2"],
        request.GET["n3"],
        request.GET["n4"],
        request.GET["n5"],
    )
    result = predict_price(float(n1), float(n2), float(n3), float(n4), float(n5))
    return render(
        request,
        "predict.html",
        {"result2": result, "n1": n1, "n2": n2, "n3": n3, "n4": n4, "n5": n5},
    )
