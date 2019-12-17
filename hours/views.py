from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from hours.models import VolunteerLog
from django.views.generic import CreateView

# Create your views here.

class HoursLogView(CreateView):
    model = VolunteerLog
    template_name = 'log-hours.html'
    fields = ('first_name', 'last_name', 'computing_id', 'hours')
    def get_success_url(self):
        return ".."
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())
def index(request):
    return render(request, "index.html")