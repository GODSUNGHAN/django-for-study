from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]


#뭔 멍멍이 소리지
#이제 post_list라는 이름의 view가 ^$ URL에 할당되었습니다.
# 이 정규표현식은 ^에서 시작해 $로 끝나는 지를 매칭할 것입니다.
# 즉 문자열이 아무것도 없는 경우만 매칭하겠죠. 틀린 것이 아니에요.
# 왜냐하면 장고 URL 확인자(resolver)는 'http://127.0.0.1:8000/'
#  는 URL의 일부가 아니기 때문입니다. 이 패턴은 장고에게 누군가 웹사이트에
#  'http://127.0.0.1:8000/' 주소로 들어왔을 때 views.post_list를
# 보여주라고 말할 거에요.

#마지막 부분인 name='post_list'는 URL에 이름을 붙인 것으로 뷰를 식별합니다.
#  뷰의 이름과 같을 수도 완전히 다를 수도 있습니다.
#  이름을 붙인 URL은 프로젝트의 후반에 사용할 거예요.
# 그러니 앱의 각 URL마다 이름 짓는 것은 중요합니다.
# URL에 고유한 이름을 붙여, 외우고 부르기 쉽게 만들어야 해요.