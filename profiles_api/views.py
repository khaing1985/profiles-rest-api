from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns  a lis"""
        result =[
            'a',
            'b',
            'c',
            'd',
        ]

        return Response({"message":"Hello","an_apiview": result})
