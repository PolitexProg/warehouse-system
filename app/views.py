from rest_framework.views import APIView
from rest_framework.response import Response
from .services import calculate_materials
from rest_framework.exceptions import ValidationError
class CalculateMaterialsView(APIView):
    def post(self, request):
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Must be a list"}, status=400)
        for item in data:
            product_code = item.get('product_code')
            if not product_code or len(str(product_code)) != 6:
                return Response({"error": "Each item must have a 'product_code' of length 6."}, status=400)
        return Response(calculate_materials(data))