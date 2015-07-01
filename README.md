# start-with-django-webframework 

# 날로 먹는 Django 웹프레임워크 강좌 따라하기

# 진행
 1. Pystagram 기획 (100%)
 2. 개발 환경 꾸리기 (100%)
 3. Photo 앱과 모델 만들기 (100%)
  - MVC and MTV : Controller -> View, View -> Template
  - MVC 패털의 Controller 역할은 Django framework 그 자체가 하고 있다.
 4. Photo 모델로 Admin 영역에서 데이터 다루기 (100%)
  - admin site 등록
  - model class 의 delete method override
 5. URL 에 view 함수 연결해서 사진 출력하기 (100%)
 6. Django 정적파일 기능 이해하기
  - STATICFILES_DIRS : 개발단계에서 정적 파일이 위치한 경로를 지정
  - MEDIA_URL, MEDIA_ROOT
 7. 사진 게시물 제출하여 게시하기
  - Form, ModelForm (fields, excludes)
  - CSRF(Cross Site Request Forgery)
  - 'DIRS': [os.path.join(BASE_DIR, 'templates')], <= 1.8
  - 대게의 경우 Django Form 이 자동으로 만들어주는 폼 항목 구성을 그대로 사용하지 않음
 8. 로그인, 로그아웃 하기
  - Authentication
  - Authorization
  - AUTH_USER_MODEL, LOGIN_REDIRECT_URL
 9. 로그인한 이용자만 사진 게시물 게시하기
