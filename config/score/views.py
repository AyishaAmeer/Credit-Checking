from django.shortcuts import render

from django.shortcuts import render
from .forms import CreditForm

def compute_score(c):
    # Not a real FICO—just a demo scoring function.
    base = 200

    total_pay = c['on_time_payments'] + c['missed_payments'] or 1
    p = c['on_time_payments'] / total_pay                # 0..1
    payment_contrib = p * 300                            # 0..300

    u = max(0.0, min(100.0, c['credit_utilization']))    # %
    util_contrib = (100 - u) * 1.5                       # 0..150 (lower is better)

    ratio = c['annual_income'] / (c['existing_debt'] + 1.0)
    ratio_score = min(100.0, ratio * 20.0)               # clamp
    ratio_contrib = ratio_score * 1.5                    # 0..150

    history_score = min(100.0, c['history_years'] * 5.0) # 20y -> 100
    history_contrib = history_score * 1.0                # 0..100

    age_score = min(100.0, max(0.0, (c['age'] - 18) / 0.82))  # 18..100 -> 0..100
    age_contrib = age_score * 0.5                        # 0..50

    raw = base + payment_contrib + util_contrib + ratio_contrib + history_contrib + age_contrib
    score = max(300, min(850, int(raw)))                 # clamp to 300..850

    if score >= 800: band = "Exceptional"
    elif score >= 740: band = "Very Good"
    elif score >= 670: band = "Good"
    elif score >= 580: band = "Fair"
    else: band = "Poor"

    return score, band

def home(request):
    result = None
    form = CreditForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        score, band = compute_score(form.cleaned_data)
        result = {"score": score, "band": band}
    return render(request, "score/home.html", {"form": form, "result": result})

