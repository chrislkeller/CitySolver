from django.conf.urls.defaults import *
from user_submit.views import index, detail, create_issue

urlpatterns = patterns('',
    url(
        regex   = r'^$',
        view    = index,
        kwargs  = {},
        name    = 'issue_table',
    ),

    url(
        regex   = r'^(?P<issue_detail_id>\d+)/$',
        view    = detail,
        kwargs  = {},
        name    = 'details_table',
    ),

    url(
        regex   = r'^submit/$',
        view    = create_issue,
        kwargs  = {},
        name    = 'issue_form',
    ),

)