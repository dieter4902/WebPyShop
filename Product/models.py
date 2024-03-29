from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User


class Product(models.Model):
    product_picture = models.ImageField(upload_to='product_pictures/', blank=False, null=True)
    COLOR_PALETTE = [
        ("#FFFFFF", "White",),
        ("#000000", "Black",),
        ("#696969", "Gray",),
        ("#A67133", "Brown",),
        ("#FF0000", "Red",),
        ("#FF8C00", "Orange",),
        ("#FFFF00", "Yellow",),
        ("#228B22", "Green",),
        ("#00FFFF", "Cyan",),
        ("#00BFFF", "Blue",),
        ("#8A2BE2", "Purple",),
        ("#FF00FF", "Pink",),
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

    color = ColorField(choices=COLOR_PALETTE,
                       default='#000000')
    price = models.FloatField()
    stars = models.FloatField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        ordering = ['name', '-price']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_votes(self):
        return Comment.objects.filter(product=self)

    def get_votes_score(self):
        votes = self.get_votes()
        if len(votes) == 0:
            return 0
        else:
            product = 0
            for element in votes:
                product += element.rating
            self.__setattr__('stars', round(product / len(votes), 2))
            self.save()
            return round(product / len(votes), 2)

    def remove_vote(self, single_rating):
        score = self.get_votes_score()
        votes = self.get_votes_count()
        endrating = round((score * votes - single_rating) * (votes - 1), 2)
        self.__setattr__('stars', endrating)
        self.save()

    def get_votes_count(self):
        return len(self.get_votes())

    def __str__(self):
        return self.name + ' (' + self.brand + ')'

    def __repr__(self):
        return self.name + ' / ' + self.brand + ' / ' + str(self.price) + "€"


class Comment(models.Model):
    text = models.TextField(max_length=500)
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reported = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def set_flag(self):
        self.reported = True
        self.save()

    def clear_flag(self):
        self.reported = False
        self.save()

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
        print(user.is_staff)
        if user == self.user or user.is_staff:
            print("e")
            self.product.remove_vote(self.rating)
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
