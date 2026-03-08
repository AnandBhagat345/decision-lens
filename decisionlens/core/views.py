from django.shortcuts import render
from .decision_engine import analyze_decision
from .models import Decision

def home(request):

    paths = None

    if request.method == "POST":

        text = request.POST.get("decision_text", "").lower()

        # save decision
        Decision.objects.create(text=text)

        # analyze decision
        paths = analyze_decision(text)
        
        # save first option risk for pattern analysis
        risk = paths[0]["risk"]

        Decision.objects.create(
            text=text,
            risk_level=risk
        )

    return render(request, "index.html", {"paths": paths})

    
def history(request):
    decisions = Decision.objects.all().order_by('-created_at')
    return render(request, "history.html", {"decisions": decisions})