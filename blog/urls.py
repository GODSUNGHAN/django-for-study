from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
#여기서 나타내는 r의 의미는 파이썬에게 문자열에 특수문자가 존재하는것을 알려준다.
