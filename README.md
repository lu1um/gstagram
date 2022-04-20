# README.md

### 04.19.

![img](README.assets/unknown.png) 

model 구상

생성

### 04.20.

- model 구현

  - ERD를 기반으로, accounts의 User모델과 articles의 모델들을 만들어주었다.

- base.html 만들기

  - bootstrap을 적용시키고, navbar를 복사 붙여넣기 해놓았다.

- settings.py

  - INSTALLED_APPS에 imagekit 추가

  ```
  AUTH_USER_MODEL = 'accounts.User'
  
  MEDIA_URL = '/media/'
  
  MEDIA_ROOT = BASE_DIR / 'media'
  
  STATIC_URL = '/static/'
  
  STATICFILES_DIRS = [BASE_DIR / 'static']
  ```

  - 위 속성들을 추가해주었다.

- gstagram/urls.py

  ```
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('articles.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  - media의 경로를 추가해줬다.

- 기본 프사 추가

  - static/accounts에 default_profile.jpg를 넣어두었다.