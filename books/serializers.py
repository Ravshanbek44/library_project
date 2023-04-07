from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializes(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError(
                {
                   "status": False,
                   "message": "kitob sarlavhasi harflardan iborat bolishi kerak"
                }
            )
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                    {
                        "status": False,
                        "message": "kitob sarlavhasi  va avtori bir cxil bolgan kitobni yuklay olmaysiz"
                    }
            )
        return data

    def validate_price(self, price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "narx xato kiritilgan"
                }
            )