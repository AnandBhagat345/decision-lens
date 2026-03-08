def analyze_decision(text):

    decision_paths = []

    if "job" in text and "startup" in text:

        decision_paths.append({
            "path": "Quit job and start startup",
            "risk": "High",
            "reason": "Financial instability and uncertainty in early business stages."
        })

        decision_paths.append({
            "path": "Keep job and start startup part-time",
            "risk": "Medium",
            "reason": "Income safety while testing business idea."
        })

        decision_paths.append({
            "path": "Build skills and research before starting",
            "risk": "Low",
            "reason": "Preparation reduces risk and improves chances of success."
        })

    elif "exam" in text or "degree" in text:

        decision_paths.append({
            "path": "Continue higher studies",
            "risk": "Low",
            "reason": "Improves long-term career opportunities."
        })

        decision_paths.append({
            "path": "Start working immediately",
            "risk": "Medium",
            "reason": "Early income but possible limited growth."
        })

    else:

        decision_paths.append({
            "path": "Analyze situation carefully",
            "risk": "Unknown",
            "reason": "Insufficient information to provide structured decision paths."
        })

    return decision_paths