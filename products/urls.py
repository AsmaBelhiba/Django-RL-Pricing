from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, ProductCategoryViewSet, ProductPriceHistoryViewSet

router = DefaultRouter() 
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', ProductCategoryViewSet, basename='category')
router.register(r'price-history', ProductPriceHistoryViewSet, basename='price-history')

urlpatterns = router.urls
