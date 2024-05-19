package com.DevicePriceClassifier.Api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import com.fasterxml.jackson.core.JsonProcessingException;


@SpringBootApplication
public class DpcApplication {

	public static void main(String[] args) throws JsonProcessingException {

	SpringApplication.run(DpcApplication.class,args);
	
}
}

