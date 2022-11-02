from datetime import timedelta, datetime

from django.shortcuts import render


def index(request):
    return render(
        request,
        "countdown/index.html",
        context={"until": datetime.now() + timedelta(seconds=60)},
    )
