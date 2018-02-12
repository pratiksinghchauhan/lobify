"""lobify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout
from login.views import home
from useraccounts.views import messageadvverification,addmoney,viewdetailsmesswise,messagedietverification,messwise,userbills,profilesettings,emailsettings,userprofile,passwordsettings,loginajax,sellerrecords,paymentdone,userrecords,verifydiet,searchuser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home),
    url(r'^logout/$', logout, {'next_page': '/home/'}, name='logout'),
    url(r'^accountsettings/', profilesettings),
    url(r'^emailsettings/', emailsettings),
    url(r'^userhome/', userprofile),
    url(r'^passwordsettings/', passwordsettings),
    url(r'^loginajax/', loginajax),
    url(r'^sellerrecords/', sellerrecords),
    url(r'^paymentdone/', paymentdone),
    url(r'^managerecords/', userrecords),
    url(r'^verifydiet/', verifydiet),
    url(r'^search/', searchuser),
    url(r'^userbills/', userbills),
    url(r'^messwise/', messwise),
    url(r'^mverify/', messagedietverification),
    url(r'^messwiselist/', viewdetailsmesswise),
    url(r'^addmoney/', addmoney),
    url(r'^adverify/', messageadvverification),

]
