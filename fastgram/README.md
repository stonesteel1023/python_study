# 만들 것

1. User API
: 로그인, 로그아웃, 회원가입
: 팔로우, 언팔로우

2. 이미지 업로드
 - 웹개발 프로젝트이기 때문에 크롬브라우저에서
 - 그외에는 구글링, 스택오버플로우 이용

 ## 개발환경 구축
 - VSC2
 - python 3.6이상
 - Django 2.0이상
 - github

 ## 프로젝트 세팅

 1) pip install django
 2) django-admin startproject fastgram .
 3) python manage.py migrate(db.sqlite3)
 4) git commit -m 'Init' (fastgram/manage.py)
 5) setting.py 
        LANGUATE_CODE = 'ko-kr'
        TIME_ZONE = 'Asia/Seoul'
    git commit -m 'Edit setting' (fastgram/setting.py)

## 설명
### Class view(CBV)
- HTTP 메소드(GET/POST)를 작성할 때 메소드명을 사용 -> 코드 간결
- 제너릭 뷰, 믹스인 사용 -> 개발 생산성, 코드 재사용 