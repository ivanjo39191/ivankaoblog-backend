from rest_framework import serializers
from.models import Travel, Rating, Place
from rest_framework.authtoken.models import Token

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
      model = Travel
      fields = ('id','title','description','rating_average','url','category','subcategory','author','comments_list')
      extra_kwargs = {'url': {'required':True}}


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Rating
      fields = ('id','stars','user','travel','comments')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
      model = Place
      fields = ('json_d', 'name', 'zone', 'toldescribe', 'description', 'add', 'zipcode', 'region', 'town', 'tel', 'travellinginfo', 'opentime', 'website', 'picture1' , 'picdescribe1', 'picture2', 'picdescribe2', 'picture3', 'picdescribe3', 'gov', 'px', 'py', 'orgpclass', 'pclass1', 'pclass2', 'pclass3', 'map', 'parkinginfo', 'parkinginfo_px', 'parkinginfo_py', 'ticketinfo', 'remarks', 'keyword', 'changetime')

class PlacePositionSerializer(serializers.ModelSerializer):
    class Meta:
      model = Place
      fields = ('json_d', 'name', 'description', 'picture1', 'px', 'py')