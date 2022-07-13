from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models import Makale
from datetime import date, datetime
from django.utils.timesince import timesince
from django.utils.timezone import localdate
from pytz import UTC


# modelSerializer


class MakaleSerializer(serializers.ModelSerializer):

    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Makale
        fields = '__all__'
        # fields= ['yazar', 'baslik' ,'aciklama']
        # exclude=['yazar', 'baslik' ,'aciklama']
        read_only_fields = ['id', 'yayinlanma_tarihi', 'guncellenme_tarihi']

    def get_time_since_pub(self, object):
        now = datetime.utcnow().replace(tzinfo=UTC)
        pub_date = object.yayinlanma_tarihi

        if object.aktif:
            time_delta = timesince(pub_date, now)
            return time_delta

        else:
            return 'Aktif değil'

    def validate_yayinlanma_tarihi(self, tarih):
        today = date.today()
        if tarih > today:
            raise serializers.ValidationError(
                'Yaınlanma tarihi bugünün tarihinden büyük olamaz. ')
        return tarih


# standart serializer
class MakaleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    aktif = serializers.BooleanField()
    yayinlanma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.yayinlanma_tarihi = validated_data.get(
            'yayinlanma_tarihi', instance.yayinlanma_tarihi)
        instance.guncellenme_tarihi = validated_data.get(
            'guncellenme_tarihi', instance.guncellenme_tarihi)
        instance.save()
        return instance

    def vaidate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError(
                'Başlık ve açıklama aynı olamaz!!!!')
        return data

    def validate_baslik(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                f'Başlık 20 karakterden kısa olamaz. Siz {len(value)} karakter girdiniz. ')
        return value
