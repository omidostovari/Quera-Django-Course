from django.db import models


class User(models.Model):
    # type your code here
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    score = models.IntegerField()

    def __str__(self):
        return self.name

    def change_name(self, input_str):
        self.name = input_str
        self.save()

    def change_password(self, input_pass):
        self.password = input_pass
        self.save()

    def change_score(self, input_score):
        self.score += input_score
        self.save()