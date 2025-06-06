from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .views import root_view 

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('rest/', include('products.urls')),  
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),


]

