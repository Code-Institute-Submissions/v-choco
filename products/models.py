from django.db import models
from django.contrib.auth.models import User


# Models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name

    def get_rating(self):
        total = sum(int(review['rating']) for review in self.reviews.values())

        return total / self.reviews.count()


class ProductReview(models.Model):
    product = models.ForeignKey(Product,
                                related_name="reviews",
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             related_name="reviews",
                             on_delete=models.CASCADE)
    content = models.CharField(max_length=254, null=True, blank=True)
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
