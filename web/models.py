from django.db import models
from django.utils import timezone

class Post(models.Model): #모델을 정의하는 코드이다. (모델은 객체 object 이다.)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#다른 모델에 대한 링크를 의미한다.
    title = models.CharField(max_length=200) #Charfiled 는글자수가 제한된 텍스트를 정의할때사용
    text = models.TextField() #글자수 제한이 없는 긴 텍스트를 위한 속성이다.
    created_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):   #호출시 포스트 모델의 제목텍스트(string)을 얻게된다.
        return self.title

