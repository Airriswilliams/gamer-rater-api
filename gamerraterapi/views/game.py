from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models import Game
from gamerraterapi.models.player import Player
from django.core.exceptions import ValidationError


class GameView(ViewSet):
    
    def retrieve(self,request,pk):
        """HANDLE GET requests for single game """
        
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        
        games = Game.objects.all()
        seralizer = GameSerializer(games, many=True)
        return Response(seralizer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
        
        
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = ('id', 'title','description', 'designer', 'year_released', 'number_of_players', 'estimated_time_to_play','recommended_age','player','category')
        depth = 1
        
class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title','description', 'designer', 'year_released', 'number_of_players', 'estimated_time_to_play','recommended_age','player','category')
