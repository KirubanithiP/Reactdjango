from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from barcode import generate
import barcode
from barcode.writer import ImageWriter


class Students(models.Model):
    studentId = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Course = models.CharField(max_length=100)

    

class Websites(models.Model):
    name = models.CharField(max_length=100)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Barcode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='barcodes/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.image:
            code128 = barcode.Code128(self.code, writer=ImageWriter())
            buffer = BytesIO()
            code128.write(buffer)
            self.image.save(f'{self.code}.png', File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code



class ExcelFile(models.Model):
    file = models.FileField(upload_to='uploads/excel_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)






