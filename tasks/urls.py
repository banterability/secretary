from django.conf.urls.defaults import *

urlpatterns = patterns('secretary.tasks.views',
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'task_archive'),
    (r'^submit/', 'submit_task'),
    (r'^$', 'tasks'),
)
