from django.conf.urls import url
from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^$',index,name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'webapp/registration/login.html'), name='login'),
    url(r'^logout/$', auth_views.LoginView.as_view(template_name = 'webapp/registration/logout.html'), name='logout'),
    url(r'^Amar/$',list_amar,name='list_amar'),
    url(r'^Amar/create/$', amar_create, name='amar_create'),
    url(r'^Amar/(?P<id>\d+)/update/$', amar_update, name='amar_update'),
    url(r'^Amar/(?P<id>\d+)/delete/$', amar_delete, name='amar_delete'),
    url(r'^Amar/Rep$',list_amar_rep,name='list_amar_rep'),
    url(r'^Amar/Rep/(?P<id>\d+)/Get$',list_amar_rep_type,name='list_amar_rep_type'),
    url(r'^Amar/ListCurrentWeek$', list_lastweek_amar, name='list_lastweek_amar'),
    url(r'^Amar/ListCurrentMonth$', list_lastmonth_amar, name='list_lastmonth_amar'),
    url(r'^Amar/ListCurrentDay$', list_lastday_amar, name='list_lastday_amar'),


    url(r'^Bedeh/$',list_bedeh,name='list_bedeh'),
    url(r'^Bedeh/create/$', bedeh_create, name='bedeh_create'),
    url(r'^Bedeh/(?P<id>\d+)/update/$', bedeh_update, name='bedeh_update'),
    url(r'^Bedeh/(?P<id>\d+)/delete/$', bedeh_delete, name='bedeh_delete'),

    url(r'^Talab/$',list_talab,name='list_talab'),
    url(r'^Talab/create/$', talab_create, name='talab_create'),
    url(r'^Talab/(?P<id>\d+)/update/$', talab_update, name='talab_update'),
    url(r'^Talab/(?P<id>\d+)/delete/$', talab_delete, name='talab_delete'),

    url(r'^Hazine/$',list_hazine,name='list_hazine'),
    url(r'^Hazine/create/$', hazine_create, name='hazine_create'),
    url(r'^Hazine/(?P<id>\d+)/update/$', hazine_update, name='hazine_update'),
    url(r'^Hazine/(?P<id>\d+)/delete/$', hazine_delete, name='hazine_delete'),
    url(r'^Hazine/ListCurrentWeek$', list_lastweek_hazine, name='list_lastweek_hazine'),
    url(r'^Hazine/ListCurrentMonth$', list_lastmonth_hazine, name='list_lastmonth_hazine'),
    url(r'^Hazine/ListCurrentDay$', list_lastday_hazine, name='list_lastday_hazine'),


    url(r'^Reports/$',getReport,name='getReport'),
    url(r'^Reports/(?P<dt>\w+)$',getReport,name='getReport'),

    url(r'^Dashboard/$',list_dashboard,name='list_dashboard'),
    url(r'^Dashboard/getMojudiAlyaf/$',getMojudiAlyaf,name='getMojudiAlyaf'),
    url(r'^Dashboard/getBedeh/$',getBedeh,name='getBedeh'),
    url(r'^Dashboard/getTalab/$',getTalab,name='getTalab'),
    url(r'^Dashboard/getHazine/$',getHazine,name='getHazine'),
    url(r'^Dashboard/getTotal/$',getTotal,name='getTotal'),
    url(r'^Dashboard/lineChart$',getLineChart,name='getLineChart'),
    url(r'^Dashboard/barChart$',getBarChart,name='getBarChart'),
    url(r'^Dashboard/pieMahsool$',getMahsoolPie,name='getMahsoolPie'),
    url(r'^Dashboard/lineHazine$',getHazineLineChart,name='getHazineLineChart'),


    ]
