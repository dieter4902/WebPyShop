from django.conf import settings
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
        votes = self.get_votes()
        if len(votes) == 0:
            return 0
        else:
            product = 0
            for element in votes:
                product += element.stars
            return product / len(votes)

    def get_votes_count(self):
        return len(self.get_votes())

    def vote(self, user, rating):
        users_vote = self.get_votes().filter(user=user)
        if users_vote.exists():
            if users_vote.get().stars == rating:
                users_vote.delete()
                return
            users_vote.delete()
        Vote.objects.create(stars=rating, user=user, product=self)

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stars) + ' on ' + self.product.name + ' by ' + self.user.name


class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def get_comment_prefix(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

    def get_upvotes(self):
        upvotes = Comment_Vote.objects.filter(up_or_down='U', comment=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Comment_Vote.objects.filter(up_or_down='D', comment=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, user, up_or_down):
        print(user)
        had_vote = ""
        for vote in self.get_downvotes():
            if vote.user == user:
                vote.delete()
                had_vote = "down"
        for vote in self.get_upvotes():
            if vote.user == user:
                vote.delete()
                had_vote = "up"
        if had_vote == up_or_down:
            return
        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'
        vote = Comment_Vote.objects.create(up_or_down=U_or_D, user=user, comment=self)

    def c_delete(self, user):
        print(user)
        if user == self.user:
            self.delete()

    def __str__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ')'

    def __repr__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ' / ' + str(self.timestamp) + ')'


class Comment_Vote(models.Model):
    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]
    up_or_down = models.CharField(max_length=1, choices=VOTE_TYPES, )
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.up_or_down + ' on ' + self.comment.text + ' by ' + self.user.username