from django.urls import path
from blog import views
urlpatterns = [
    path("", views.index, name="index-page"),
    # path("test-page/", views.test_page, name="test-page"),
    path("contacts/", views.contacts, name="contacts-page"),
    path("about/", views.about, name="about-page")
    # path('admin/', admin.site.urls),
]