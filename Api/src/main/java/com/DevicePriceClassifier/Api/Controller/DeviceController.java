package com.DevicePriceClassifier.Api.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import com.DevicePriceClassifier.Api.Model.Devices;
import com.DevicePriceClassifier.Api.Service.DeviceService;
import com.fasterxml.jackson.core.JsonProcessingException;

@RestController
public class DeviceController {

    @Autowired
    private DeviceService deviceService;

    @GetMapping("/devices/{id}")
    public String getDeviceDetails(@PathVariable String id){
        return deviceService.getDeviceDetails(id);
    }

    @PostMapping("/devices")
    public String addDevice(@RequestBody Devices devices) throws JsonProcessingException {
        return deviceService.addDevice(devices);
    }

    @PostMapping("/devices/")
    public String getAllDevices(){
        return deviceService.getAllDevices();
    }

    @PostMapping("/predict/{id}")
    public String predictDevicePrice(@PathVariable String id){
        return deviceService.predictDevicePrice(id);
    }
}