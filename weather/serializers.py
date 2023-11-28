##Sample serializer

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework import serializers

from .models import Eds, Counties


class ElectoralDistrictsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Eds

        fields = '__all__'

        geo_field = 'geom'


class CountiesSerializer(GeoFeatureModelSerializer):
    distance = serializers.CharField()

    class Meta:
        model = Counties

        fields = '__all__'

        geo_field = 'geom'