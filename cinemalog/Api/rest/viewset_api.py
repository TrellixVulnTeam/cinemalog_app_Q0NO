from rest_framework import viewsets
from rest_framework import permissions
from cinemalog.Api.rest.serializers import QuestionSerializer,CompetitionSerializer
from cinemalog.models import Question,Competition
from cinemalog.Api.rest.permissions import IsOwnerOrReadOnly

class QuestionViewSet(viewsets.ModelViewSet):
    
    """
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list` and `detail` actions.
    
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    
    """
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

    
class CompetitionViewSet(viewsets.ModelViewSet):
    
    """
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list` and `detail` actions.
    
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    
    """
    queryset=Competition.objects.all()
    serializer_class=CompetitionSerializer
