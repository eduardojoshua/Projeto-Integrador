from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def superuser_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('login'))
        return view_func(request, *args, **kwargs)
    return wrapper
