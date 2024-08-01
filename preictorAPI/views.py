from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Device
from .ml_model import predict_price, preprocess_features, scale_features
from .serializers import DeviceSerializer


@api_view(['GET'])
def get_all_devices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_device(request, id):
    try:
        device = Device.objects.get(id=id)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DeviceSerializer(device)
    return Response(serializer.data)

@api_view(['POST'])
def add_device(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView 
 
class PredictPrice(APIView):
    def post(self, request): 
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data 
            
            # Preprocess the data
            df = preprocess_features(data)
            df = scale_features(df)
            
            # Predict the price
            prediction = predict_price(df)
            
            return Response({'price_range': prediction}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)