# Create your views here
from datetime import datetime, date, time, timedelta
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext
from user_submit.models import issue_detail
from user_submit.models import issue_form

# the main index request
def index(request):
   startdate = date.today()
   enddate = timedelta(days=14)
   displaydate = startdate - enddate
   issue_listing = issue_detail.objects.filter(user_date_submitted__gte=displaydate)
   return render_to_response('issue_table.html', {'issue_listing': issue_listing})

# details request
def detail(request, issue_detail_id):
    p = get_object_or_404(issue_detail, pk=issue_detail_id)
    return render_to_response('details_table.html', {'issue': p},
        context_instance=RequestContext(request))

# issue form post
def create_issue(request):
    if request.method == 'POST':
            form = issue_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                form = ServerForm()
    return render_to_response('issue_form.html', {'issue_form': issue_form},
        context_instance=RequestContext(request))