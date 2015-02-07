from rest_framework import serializers 
from gamestore.models import * 

class ScoreSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Scores
		fields = ('high_score_1', 'high_score_2', 'high_score_3', 'high_score_4', 'high_score_5')
