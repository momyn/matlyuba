from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('', views.lookbook, name='lookbook'),
    path('', views.look, name='look'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail')
]


# urlpatterns = [
#     path(r'', views.product_list, name='product_list'),
#     # path('', views.product_list, name='product_list'),
#     path('<slug:category_slug>/', views.product_list,
#          name='product_list_by_category'
#          ),
#     path('<int:id>/<slug:slug>', views.product_detail,
#          name='product_detail')
# ]



# from . import views
#
# urlpatterns = [
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_slug>[-\w]+)/$',
#         views.product_list,
#         name='product_list_by_category'),
#     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
#         views.product_detail,
#         name='product_detail'),
#     url(r'^', include('app.urls', namespace='app')),
# ]
