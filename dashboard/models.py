import qrcode
import string
import random
from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Discount(models.Model):
    all_sum = models.FloatField()
    all_quantity = models.FloatField()


class Client(models.Model):
    card_id = models.ImageField(upload_to='img/client/', blank=True, null=True)
    name = models.CharField(max_length=255)
    car_number = models.CharField(max_length=8)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    bonus = models.IntegerField()

    def save(self, *args, **kwargs):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        all = lower + upper + num

        temp = random.sample(all, 10)

        password = "".join(temp)

        qrcode_img = qrcode.make(password)
        canvas = Image.new('RGB', (300, 300), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'{self.name}, {self.car_number} qr_code' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.card_id.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Klient'

class CarWash(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sum = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Moyka'
