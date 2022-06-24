from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User


class Product(models.Model):
    COLOR_PALETTE = [
        ("#FFFFFF", "white",),
        ("#000000", "black",),
    ]

    MATERIALS = [
        ("p", "Plüsch",),
        ("s", "Samt",)
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=420)
    height = models.IntegerField(default=0,
                                 validators=[  # in cm
                                     MaxValueValidator(500),
                                     MinValueValidator(0)
                                 ])
    width = models.IntegerField(default=0,
                                validators=[  # in cm
                                    MaxValueValidator(500),
                                    MinValueValidator(0)
                                ])
    length = models.IntegerField(default=0,
                                 validators=[  # in cm
                                     MaxValueValidator(500),
                                     MinValueValidator(0)
                                 ])
    weight = models.IntegerField(default=0,
                                 validators=[  # in kilo
                                     MaxValueValidator(1000),
                                     MinValueValidator(0)
                                 ])

    color = ColorField(choices=COLOR_PALETTE,
                       default='#000000')

    material = models.CharField(max_length=1,
                                choices=MATERIALS, )
    stockwerke = models.IntegerField(default=1,
                                     validators=[
                                         MaxValueValidator(20),
                                         MinValueValidator(-3)
                                     ])
    hoehlen = models.IntegerField(default=1,
                                  validators=[
                                      MaxValueValidator(20),
                                      MinValueValidator(-3)
                                  ])
    price = models.IntegerField()

    class Meta:
        ordering = ['name', '-price']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_votes(self):
        return Vote.objects.filter(product=self)

    def get_votes_score(self):
        score = self.get_votes()
        product = 0
        for element in score:
            product += element.stars
        return product / len(score)

    def get_votes_count(self):
        return len(self.get_votes())

    def vote(self, user, num_stars):
        users_vote = self.get_votes().filter(user=user)
        if users_vote.exists():
            users_vote.delete()
        Vote.objects.create(stars=num_stars, user=user, product=self)

    def __str__(self):
        return self.name + ' (' + self.brand + ')'

    def __repr__(self):
        return self.name + ' / ' + self.brand + ' / ' + str(self.price) + "€"


class Vote(models.Model):
    stars = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stars) + ' on ' + self.product.name + ' by ' + self.user.username
