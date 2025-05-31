from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.management import call_command
from .serializers import ProductSerializer, ProductCategorySerializer, ProductPriceHistorySerializer
from .models import Product, ProductCategory, ProductPriceHistory
from .throttles import PricingRateThrottle
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.models import AccessToken



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['pricing.read'] 
    throttle_classes = [PricingRateThrottle]

    def get_permissions(self):
        print("== Debug: Required scopes =", self.required_scopes)
        print("== Debug: Token (request.auth) =", self.request.auth)
        print("== Debug: User =", self.request.user)
        if isinstance(self.request.auth, AccessToken):
            print("== Debug: Token scope =", self.request.auth.scope)
        return super().get_permissions()

    @action(detail=False, methods=['get'], throttle_classes=[PricingRateThrottle])
    def current_prices(self, request):
        """
        Custom endpoint to retrieve product name and current price.
        """
        products = Product.objects.all()
        data = [{"id": p.id, "name": p.name, "current_price": p.current_price} for p in products]
        return Response(data)

    @action(detail=False, methods=['post'], throttle_classes=[PricingRateThrottle])
    def trigger_price_update(self, request):
        """
        Custom endpoint to trigger the price update via management command.
        """
        try:
            call_command('update_prices')
            return Response({'message': 'Price update triggered successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductPriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProductPriceHistory.objects.all()
    serializer_class = ProductPriceHistorySerializer
