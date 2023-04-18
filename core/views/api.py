from ..models import Candidate
from ..serializers import CandidateSerialize

from rest_framework.viewsets import ModelViewSet

class CandiitateApiViewSet(ModelViewSet):
    queryset = Candidate.objects.all().order_by('-quantity_votes')
    serializer_class = CandidateSerialize
