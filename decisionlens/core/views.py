from django.shortcuts import render

def home(request):
    result = None

    if request.method == "POST":
        text = request.POST.get("decision_text", "").lower()

        if "job" in text and "startup" in text:
            result = "Career Decision Detected: Job vs Startup. Risk may be high depending on savings."
        elif "exam" in text or "degree" in text:
            result = "Education Decision Detected. Long-term reward possible."
        elif "loan" in text or "money" in text:
            result = "Finance Decision Detected. Evaluate repayment capacity."
        else:
            result = "General Decision Detected. More analysis needed."

    return render(request, "index.html", {"result": result})