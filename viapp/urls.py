"""viapp URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework import routers
from django.conf import settings
from image_metadata import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^', include(router.urls)),
    url(r'^image_metadata/', views.image_metadata),
    url(r'^image/annotate',  views.handle_annotation),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]

"""
in db: "{\"https://upload.wikimedia.org/wikipedia/commons/6/62/Farmer_in_Tamil_Nadu_1993.JPG\":{\"fileref\":\"\",\"size\":0,\"filename\":\"https://upload.wikimedia.org/wikipedia/commons/6/62/Farmer_in_Tamil_Nadu_1993.JPG\",\"base64_img_data\":\"\",\"file_attributes\":{},\"regions\":{\"0\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":676,\"y\":173,\"width\":320,\"height\":618},\"region_attributes\":{\"name\":\"hello\"}},\"1\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":501,\"y\":282,\"width\":56,\"height\":139},\"region_attributes\":{}}}},\"https://upload.wikimedia.org/wikipedia/commons/c/cb/Rescue_exercise_RCA_2012.jpg\":{\"fileref\":\"\",\"size\":0,\"filename\":\"https://upload.wikimedia.org/wikipedia/commons/c/cb/Rescue_exercise_RCA_2012.jpg\",\"base64_img_data\":\"\",\"file_attributes\":{},\"regions\":{\"0\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":1078,\"y\":341,\"width\":708,\"height\":548},\"region_attributes\":{}},\"1\":{\"shape_attributes\":{\"name\":\"polygon\",\"all_points_x\":[599,337,405,468,990,1218,1272,1616,1633,1145,1165,1386,1395,1325,1291,1145,1024,908,893,975,837,502,340,340,345,345,345,599],\"all_points_y\":[643,570,286,306,308,265,294,233,289,345,388,454,514,561,633,643,650,636,621,602,580,563,568,568,573,573,573,643]},\"region_attributes\":{\"name\":\"Helicopter\"}},\"2\":{\"shape_attributes\":{\"name\":\"polygon\",\"all_points_x\":[599,337,405,468,990,1218,1272,1616,1633,1145,1165,1386,1395,1325,1291,1145,1024,908,893,975,837,502,340,340,345,345,345,599],\"all_points_y\":[643,570,286,306,308,265,294,233,289,345,388,454,514,561,633,643,650,636,621,602,580,563,568,568,573,573,573,643]},\"region_attributes\":{\"name\":\"Helicopter\"}},\"3\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":1096,\"y\":887,\"width\":76,\"height\":152},\"region_attributes\":{\"name\":\"man\"}},\"4\":{\"shape_attributes\":{\"name\":\"polygon\",\"all_points_x\":[1003,1090,1484,1801,2085,2190,2193,2207,2190,2182,2104,2035,2015,2001,1974,1990,1960,1912,1901,1890,1865,1846,1837,1776,1785,1729,1584,1493,1457,1142,1104,1095,1003],\"all_points_y\":[1129,1276,1315,1315,1331,1309,1226,1198,1193,1131,1120,1101,1084,1120,1117,806,587,575,726,756,756,492,756,862,912,959,967,990,1051,1045,1059,1104,1129]},\"region_attributes\":{\"name\":\"boat\"}}}},\"https://upload.wikimedia.org/wikipedia/commons/9/99/Four_pears.jpg\":{\"fileref\":\"\",\"size\":0,\"filename\":\"https://upload.wikimedia.org/wikipedia/commons/9/99/Four_pears.jpg\",\"base64_img_data\":\"\",\"file_attributes\":{},\"regions\":{\"0\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":593,\"y\":1189,\"width\":337,\"height\":385},\"region_attributes\":{}},\"1\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":1593,\"y\":1230,\"width\":359,\"height\":237},\"region_attributes\":{}},\"2\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":2611,\"y\":1200,\"width\":333,\"height\":248},\"region_attributes\":{}},\"3\":{\"shape_attributes\":{\"name\":\"rect\",\"x\":3548,\"y\":1041,\"width\":170,\"height\":207},\"region_attributes\":{\"name\":\"Modified\"}}}}}"


"""