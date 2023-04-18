from rest_framework import serializers
from .models import Candidate
class CandidateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','name','political_party','number','quantity_votes']