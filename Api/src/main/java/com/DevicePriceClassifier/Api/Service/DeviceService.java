package com.DevicePriceClassifier.Api.Service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.*;
import com.DevicePriceClassifier.Api.Model.Devices;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@Service
public class DeviceService {

    private static final String API_URL = "http://127.0.0.1:8000/api/";

    public String getDeviceDetails(String id){
        RestTemplate restTemplate = new RestTemplate();
        String url = API_URL + "devices/" + id;

        ResponseEntity<String> response = restTemplate.getForEntity(url, String.class);

        return response.getBody();
    }

    public String addDevice(Devices devices) throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        String jsonDevices = mapper.writeValueAsString(devices);

        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<String> requestEntity = new HttpEntity<>(jsonDevices, headers);

        ResponseEntity<String> response = restTemplate.postForEntity(API_URL + "adddevices", requestEntity, String.class);

        return response.getBody();
    }

    public String getAllDevices(){
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        HttpEntity<String> entity = new HttpEntity<>(headers);

        ResponseEntity<String> response = restTemplate.exchange(API_URL + "devices", HttpMethod.POST, entity, String.class);

        return response.getBody();
    }

    public String predictDevicePrice(String id){
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        HttpEntity<String> entity = new HttpEntity<>(headers);

        ResponseEntity<String> response = restTemplate.exchange(API_URL + "predict/" + id + "/", HttpMethod.POST, entity, String.class);

        return response.getBody();
    }
}
