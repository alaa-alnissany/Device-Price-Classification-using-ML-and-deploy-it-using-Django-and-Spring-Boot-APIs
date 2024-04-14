from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from restful_api.models import Device
from .serializers import DeviceSerializer
from rest_framework import status
import joblib
import pandas as pd

model = joblib.load('models/pipe.joblib')

@api_view(['POST'])
def get_all_devices(request):
    try:
        # Retrieve all devices from the database
        devices = Device.objects.all()

        # Serialize the devices using DeviceSerializer
        serializer = DeviceSerializer(devices, many=True)

        return Response(serializer.data)
    except Exception as e:
        # Handle any exceptions (e.g., database errors)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_device_details(request, device_id):
    """
    Retrieve details of a specific device by ID.

    Args:
        request: The HTTP request object.
        device_id (int): The ID of the device to retrieve.

    Returns:
        Response: A Response containing the device details.
    """
    try:
        # Retrieve the device with the given ID
        device = Device.objects.get(pk=device_id)

        # Serialize the device using DeviceSerializer
        serializer = DeviceSerializer(device)

        return Response(serializer.data)
    except Device.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Handle any other exceptions (e.g., database errors)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_device(request):
    """
    Add a new device.

    Args:
        request: The HTTP request object.

    Returns:
        Response: A Response containing the newly created device data.
    """
    try:
        # Deserialize the request data using DeviceSerializer
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new device to the database
            serializer.save()

            # Return the serialized data of the newly created device
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # Handle any other exceptions (e.g., database errors)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def predict_device_price(request, device_id):
    # Retrieve the device with the given ID
    device = get_object_or_404(Device, pk=device_id)
    
    
    def true_false(str_:bytes):
        if str_ == b'True':
            return True
        else:
            return False
     
    # Prepare input data for prediction (use your actual feature names)
    input_data = {
        "battery_power" : [device.battery_power],
        "blue" : [true_false(device.blue)],
        "clock_speed" : [device.clock_speed],
        "dual_sim" : [true_false(device.dual_sim)],
        "fc" : [device.fc],
        "four_g" : [true_false(device.four_g)],
        "int_memory" : [device.int_memory],
        "m_dep" : [device.m_dep],
        "mobile_wt" : [device.mobile_wt],
        "n_cores" : [device.n_cores],
        "pc": [device.pc],
        "px_height" : [device.px_height],
        "px_width" : [device.px_width],
        "ram" : [device.ram],
        "sc_h" : [device.sc_h],
        "sc_w" : [device.sc_w],
        "talk_time" : [device.talk_time],       
        "three_g" : [true_false(device.tree_g)],
        "touch_screen" : [true_false(device.touch_screen)],       
        "wifi" : [true_false(device.wifi)],
    }

    input_data = pd.DataFrame.from_dict(input_data)

    try:
        # Make the prediction using the loaded model
        predicted_price_range = model.predict(input_data)[0]

        # Save the predicted price in the device entity
        device.price_range = predicted_price_range
        device.save()

        # Return the predicted price as a JSON response
        return JsonResponse({'predicted_price': str(predicted_price_range)})
    
    except Exception as e:
        # Handle any exceptions (e.g., invalid input data)
        return JsonResponse({'error': str(e)}, status=400)
