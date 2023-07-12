from django.urls import path
from blog import views
urlpatterns = [
    path("", views.index, name="index-page"),
    # path("test-page/", views.test_page, name="test-page"),
    path("contacts/", views.contacts, name="contacts-page"),
    path("about/", views.about, name="about-page"),
    path("post/<int:pk>", views.get_post_detail, name="post-detail"),
    path("post/update/<int:pk>", views.post_update, name="post-update"),
    path("post/delete/<int:pk>", views.post_delete, name="post-delete"),
    # path('admin/', admin.site.urls),
]