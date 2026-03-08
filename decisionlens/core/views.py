from django.shortcuts import render
from .decision_engine import analyze_decision


def home(request):

    paths = None

    if request.method == "POST":

        text = request.POST.get("decision_text", "").lower()
        paths = analyze_decision(text)

    return render(request, "index.html", {"paths": paths})