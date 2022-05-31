from http.client import HTTPResponse
from typing import Callable

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def login_required_to_view(function: Callable) -> Callable:
    """Decorator for any show_content view to prevent unauthorized users from seeing private content"""

    def _function(request: HttpRequest, *args, **kwargs) -> any:
        if not request.user.is_authenticated:
            messages.info(request, 'Login to view services!')
            return HttpResponseRedirect(reverse('login_page'))
        return function(request, *args, **kwargs)

    return _function
