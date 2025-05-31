from django.core.management.base import BaseCommand
from products.models import Product  
from ...trainer import PricingModelTrainer  

class Command(BaseCommand):
    help = 'Retrain RL models for all products using the given timesteps.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--timesteps',
            type=int,
            default=1000,
            help='Number of timesteps for training the RL model'
        )

    def handle(self, *args, **options):
        timesteps = options['timesteps']
        products = Product.objects.filter(pricing_strategy='RL')

        if not products.exists():
            self.stdout.write(self.style.WARNING("⚠️ No RL products found."))
            return

        for product in products:
            try:
                trainer = PricingModelTrainer(product.id)
                trainer.train(total_timesteps=timesteps)
                self.stdout.write(self.style.SUCCESS(f"✅ Trained RL model for product {product.name}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Failed to train model for {product.name}: {e}"))
