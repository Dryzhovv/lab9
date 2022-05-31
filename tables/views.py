from typing import Type

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import CreateUserForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from easytables.forms import CreateUserForm, PlanesForm, FlightsRoutes
from easytables.utils import login_required_to_view
from tables.models import Flight, Plane


def home(request: HttpRequest) -> render:
    return render(request, 'home.html', {})


@login_required_to_view
def show_flights_routes(request: HttpRequest) -> render:
    """" Shows flights routes """

    flights = Flight.objects.all()  # noqa
    page = request.GET.get('page', 1)
    limit = request.POST.get('limit', 3)
    paginator = Paginator(flights, limit)

    try:
        flights = paginator.page(page)
    except PageNotAnInteger:
        flights = paginator.page(1)
    except EmptyPage:
        flights = paginator.page(paginator.num_pages)

    return render(request, 'show_flights_routes.html', {
        'flights': flights,
    })


@login_required_to_view
def show_planes(request: HttpRequest) -> render:
    """Show planes"""

    planes = Plane.objects.all()  # noqa
    page = request.GET.get('page', 1)
    limit = request.POST.get('limit', 3)
    paginator = Paginator(planes, limit)

    try:
        planes = paginator.page(page)
    except PageNotAnInteger:
        planes = paginator.page(1)
    except EmptyPage:
        planes = paginator.page(paginator.num_pages)

    return render(request, 'show_planes.html', {
        'planes': planes,
    })


def registration_page(request: HttpRequest) -> HttpResponse:
    """Registrate user"""
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_page')
    context = {'form': form, }
    return render(request, 'register.html', context)


def login_page(request: HttpRequest) -> HttpResponse:
    """Login in user"""
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = redirect('home')
                messages.success(request, 'Logged in')
                response.set_cookie('username', username)
                response.set_cookie('login_status', True)
                return response
            else:
                messages.info(request, 'Credentials are incorrect')

        context = {}
        return render(request, 'login.html', context)


def logout_page(request: HttpRequest) -> HttpResponse:
    """Logout user"""
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('login_page')


def password_success(request: HttpRequest) -> HttpResponse:
    return render(request, 'password_success.html', {})


class PasswordChangedView(PasswordChangeView):
    """Password change page"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def add_plane(request: HttpRequest) -> HttpResponseRedirect:
    """Add plane to database"""
    submitted = False
    if request.method == 'POST':
        form = PlanesForm(request.POST)
        form.type = request.POST.get('plane_type')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tables/add_plane?submitted=True')

    form = PlanesForm
    if 'submitted' in request.GET:
        submitted = True

    return render(request, 'add_plane.html', {
        'form': form,
        'submitted': submitted,
    })


def add_flights_routes(request: HttpRequest) -> HttpResponse:
    """Add flight_routes to database"""
    submitted = False
    if request.method == 'POST':
        form = FlightsRoutes(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tables/add_flights_routes?submitted=True')

    form = FlightsRoutes
    if 'submitted' in request.GET:
        submitted = True

    return render(request, 'add_flights_routes.html', {
        'form': form,
        'submitted': submitted,
    })
