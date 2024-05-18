from fastapi import Body, FastAPI, Response,status,HTTPException

app = FastAPI()
from pydantic import BaseModel


class Car(BaseModel):
    id: int
    name: str
    kilometers_per_liter: float
    miles_per_gallon: float
    cylinders: int
    displacement: float
    horsepower: int
    torque: int
    weight_in_lbs: int
    acceleration: float
    top_speed: int
    year: str
    origin: str
    transmission: str
    drive_type: str
    fuel_type: str
    fuel_tank_capacity: int
    length: int
    width: int
    height: int
    wheelbase: int
    cargo_capacity: int
    seating_capacity: int
    infotainment_system: str
    safety_features: list[str]
    interior_features: list[str]
    exterior_features: list[str]
    co2_emissions: int
    fuel_efficiency_rating: str
    warranty: str
    maintenance_schedule: str
    resale_value: str
    image: str

def find_car(id):
    for car in my_cars:
        if car['id'] == id:
            return car


my_cars = [
    {
        "id":1,
        "Name": "Toyota Land Cruiser Prado",
        "Kilometers_per_Liter": 12 ,
        "Miles_per_Gallon": 28 ,
        "Cylinders": 6,
        "Displacement": 3.5,
        "Horsepower": 210,
        "Torque": 267,
        "Weight_in_lbs": 5500,
        "Acceleration": 11,
        "Top_Speed": 109,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic",
        "Drive_Type": "4WD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 87,
        "Length": 191,
        "Width": 76,
        "Height": 74,
        "Wheelbase": 110,
        "Cargo_Capacity": 16,
        "Seating_Capacity": 7,
        "Infotainment_System": "8-inch touchscreen with navigation",
        "Safety_Features": ["Airbags", "ABS", "Lane Assist", "Blind Spot Monitor"],
        "Interior_Features": ["Leather seats", "Climate control", "Heated seats"],
        "Exterior_Features": ["Sunroof", "Alloy wheels", "Fog lights"],
        "CO2_Emissions": 295,
        "Fuel_Efficiency_Rating": "D",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 15% per year",
        "Image": "https://i.ibb.co/v3Bmm9x/ladimir-ladroid-Cy-Ey-Jjfgd5-A-unsplash.jpg" 
        
    },
    {
        "id":2,
        "Name": "Mazda Demio (Mazda 2)",
        "Kilometers_per_Liter": 18.0,
        "Miles_per_Gallon": 42.3,
        "Cylinders": 4,
        "Displacement": "1.3L - 1.5L",
        "Horsepower": "60 - 100",
        "Torque": "90 - 111",
        "Weight_in_lbs": 2300,
        "Acceleration": 12,
        "Top_Speed": 115,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic/Manual",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 45,
        "Length": 161,
        "Width": 67,
        "Height": 59,
        "Wheelbase": 101,
        "Cargo_Capacity": 13,
        "Seating_Capacity": 5,
        "Infotainment_System": "7-inch touchscreen with Apple CarPlay/Android Auto",
        "Safety_Features": ["Airbags", "ABS", "Traction Control"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Alloy wheels"],
        "CO2_Emissions": 120,
        "Fuel_Efficiency_Rating": "A",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image":"https://i.ibb.co/0n5WNV3/demio.jpg"
    },
    {
        "id":3,
        "Name": "Subaru Forester",
        "Kilometers_per_Liter": 13.5,
        "Miles_per_Gallon": 31.8,
        "Cylinders": 4,
        "Displacement": "2.0L",
        "Horsepower": "150 - 260",
        "Torque": "198 - 277",
        "Weight_in_lbs": 3700,
        "Acceleration": 9.5,
        "Top_Speed": 125,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "CVT",
        "Drive_Type": "AWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 60,
        "Length": 182,
        "Width": 71,
        "Height": 68,
        "Wheelbase": 105,
        "Cargo_Capacity": 35,
        "Seating_Capacity": 5,
        "Infotainment_System": "8-inch touchscreen with navigation",
        "Safety_Features": ["Airbags", "ABS", "EyeSight Driver Assist"],
        "Interior_Features": ["Leather seats", "Dual-zone climate control"],
        "Exterior_Features": ["Sunroof", "Alloy wheels", "Roof rails"],
        "CO2_Emissions": 180,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 6,000 miles",
        "Resale_Value": "Depreciates 18% per year",
        "Image":"https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":4,
        "Name": "Toyota Hilux",
        "Kilometers_per_Liter": 12.0,
        "Miles_per_Gallon": 28.2,
        "Cylinders": "4 or 6",
        "Displacement": "2.4L - 2.8L (4-cylinder), 3.0L (6-cylinder)",
        "Horsepower": "140 - 240",
        "Torque": "253 - 376",
        "Weight_in_lbs": 4800,
        "Acceleration": 13,
        "Top_Speed": 105,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic/Manual",
        "Drive_Type": "4WD",
        "Fuel_Type": "Diesel",
        "Fuel_Tank_Capacity": 80,
        "Length": 210,
        "Width": 72,
        "Height": 72,
        "Wheelbase": 122,
        "Cargo_Capacity": 35,
        "Seating_Capacity": 5,
        "Infotainment_System": "7-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS", "Stability Control"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 210,
        "Fuel_Efficiency_Rating": "C",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 18% per year",
        "Image":"https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":5,
        "Name": "Nissan X-Trail",
        "Kilometers_per_Liter": 14.5,
        "Miles_per_Gallon": 34.1,
        "Cylinders": 4,
        "Displacement": "2.0L",
        "Horsepower": "140 - 180",
        "Torque": "147 - 177",
        "Weight_in_lbs": 3500,
        "Acceleration": 11,
        "Top_Speed": 119,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "CVT",
        "Drive_Type": "AWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 60,
        "Length": 182,
        "Width": 72,
        "Height": 70,
        "Wheelbase": 106,
        "Cargo_Capacity": 32,
        "Seating_Capacity": 5,
        "Infotainment_System": "7-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS", "Blind Spot Warning"],
        "Interior_Features": ["Cloth seats", "Manual air conditioning"],
        "Exterior_Features": ["Alloy wheels", "LED headlights"],
        "CO2_Emissions": 170,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image":"https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":6,
        "Name": "Mitsubishi Pajero Sport",
        "Kilometers_per_Liter": 9.0,
        "Miles_per_Gallon": 21.2,
        "Cylinders": 6,
        "Displacement": "3.0L - 3.5L",
        "Horsepower": "180 - 240",
        "Torque": "265 - 324",
        "Weight_in_lbs": 5000,
        "Acceleration": 12,
        "Top_Speed": 112,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic",
        "Drive_Type": "4WD",
        "Fuel_Type": "Diesel",
        "Fuel_Tank_Capacity": 70,
        "Length": 190,
        "Width": 75,
        "Height": 72,
        "Wheelbase": 110,
        "Cargo_Capacity": 23,
        "Seating_Capacity": 7,
        "Infotainment_System": "8-inch touchscreen with navigation",
        "Safety_Features": ["Airbags", "ABS", "Hill Start Assist"],
        "Interior_Features": ["Leather seats", "Climate control"],
        "Exterior_Features": ["Alloy wheels", "LED headlights"],
        "CO2_Emissions": 220,
        "Fuel_Efficiency_Rating": "C",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 6,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image":"https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":7,
        "Name": "Isuzu D-Max",
        "Kilometers_per_Liter": 13.0,
        "Miles_per_Gallon": 30.6,
        "Cylinders": 4,
        "Displacement": "2.5L",
        "Horsepower": "136 - 150",
        "Torque": "320 - 380",
        "Weight_in_lbs": 4600,
        "Acceleration": 13.5,
        "Top_Speed": 110,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic/Manual",
        "Drive_Type": "4WD",
        "Fuel_Type": "Diesel",
        "Fuel_Tank_Capacity": 76,
        "Length": 206,
        "Width": 74,
        "Height": 69,
        "Wheelbase": 123,
        "Cargo_Capacity": 38,
        "Seating_Capacity": 5,
        "Infotainment_System": "7-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS", "Traction Control"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 210,
        "Fuel_Efficiency_Rating": "C",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 6,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image":"https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":8,
        "Name": "Toyota Premio",
        "Kilometers_per_Liter": 16.0,
        "Miles_per_Gallon": 37.7,
        "Cylinders": 4,
        "Displacement": "1.8L",
        "Horsepower": "136 - 143",
        "Torque": "126 - 128",
        "Weight_in_lbs": 3000,
        "Acceleration": 12,
        "Top_Speed": 112,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "CVT",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 60,
        "Length": 182,
        "Width": 68,
        "Height": 57,
        "Wheelbase": 106,
        "Cargo_Capacity": 15,
        "Seating_Capacity": 5,
        "Infotainment_System": "7-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS", "Traction Control"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Alloy wheels"],
        "CO2_Emissions": 165,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image":"https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":9,
        "Name": "Nissan Matatu (converted vans)",
        "Kilometers_per_Liter": "10.0 - 15.0",
        "Miles_per_Gallon": "23.5 - 35.3",
        "Cylinders": "4 or 6",
        "Displacement": "2.0L - 4.0L",
        "Horsepower": "100 - 200",
        "Torque": "135 - 280",
        "Weight_in_lbs": "Varies",
        "Acceleration": "Varies",
        "Top_Speed": "Varies",
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic/Manual",
        "Drive_Type": "RWD/FWD",
        "Fuel_Type": "Petrol/Diesel",
        "Fuel_Tank_Capacity": "Varies",
        "Length": "Varies",
        "Width": "Varies",
        "Height": "Varies",
        "Wheelbase": "Varies",
        "Cargo_Capacity": "Varies",
        "Seating_Capacity": "Varies",
        "Infotainment_System": "Varies",
        "Safety_Features": ["Airbags", "ABS", "Stability Control"],
        "Interior_Features": ["Fabric seats", "Air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": "Varies",
        "Fuel_Efficiency_Rating": "Varies",
        "Warranty": "Varies",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Varies",
        "Image":"https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":10,
        "Name": "Toyota Vitz",
        "Kilometers_per_Liter": 20,
        "Miles_per_Gallon": 47,
        "Cylinders": 4,
        "Displacement": "1.0L - 1.5L",
        "Horsepower": "69 - 99",
        "Torque": "90 - 120",
        "Weight_in_lbs": 2000,
        "Acceleration": 11,
        "Top_Speed": 110,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic/CVT",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 42,
        "Length": 155,
        "Width": 66,
        "Height": 60,
        "Wheelbase": 98,
        "Cargo_Capacity": 10,
        "Seating_Capacity": 5,
        "Infotainment_System": "6-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 100,
        "Fuel_Efficiency_Rating": "A",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image": "https://example.com/toyota_vitz.jpg"
    },
    {
        "id":11,
        "Name": "Nissan Serena",
        "Kilometers_per_Liter": 10.0,
        "Miles_per_Gallon": 23.5,
        "Cylinders": 4,
        "Displacement": "2.0L - 2.5L",
        "Horsepower": "136 - 170",
        "Torque": "200 - 240",
        "Weight_in_lbs": 3600,
        "Acceleration": 13,
        "Top_Speed": 105,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 60,
        "Length": 186,
        "Width": 72,
        "Height": 70,
        "Wheelbase": 112,
        "Cargo_Capacity": 20,
        "Seating_Capacity": 8,
        "Infotainment_System": "8-inch touchscreen with navigation",
        "Safety_Features": ["Airbags", "ABS", "Lane Departure Warning"],
        "Interior_Features": ["Fabric seats", "Tri-zone climate control"],
        "Exterior_Features": ["LED headlights", "Alloy wheels"],
        "CO2_Emissions": 180,
        "Fuel_Efficiency_Rating": "C",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 18% per year",
        "Image": "https://example.com/nissan_serena.jpg"
    },
    {
        "id":12,
        "Name": "Toyota Probox",
        "Kilometers_per_Liter": 15.0,
        "Miles_per_Gallon": 35.3,
        "Cylinders": 4,
        "Displacement": "1.3L - 1.5L",
        "Horsepower": "90 - 110",
        "Torque": "100 - 120",
        "Weight_in_lbs": 2400,
        "Acceleration": 14,
        "Top_Speed": 100,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic/Manual",
        "Drive_Type": "RWD/FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 45,
        "Length": 169,
        "Width": 66,
        "Height": 64,
        "Wheelbase": 100,
        "Cargo_Capacity": 20,
        "Seating_Capacity": 5,
        "Infotainment_System": "4-inch display",
        "Safety_Features": ["Airbags", "ABS"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 150,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 15% per year",
        "Image": "https://example.com/toyota_probox.jpg"
    },
    {
        "id":13,
        "Name": "Toyota Noah",
        "Kilometers_per_Liter": 12.0,
        "Miles_per_Gallon": 28.2,
        "Cylinders": 4,
        "Displacement": "2.0L - 2.2L",
        "Horsepower": "150 - 170",
        "Torque": "180 - 200",
        "Weight_in_lbs": 3500,
        "Acceleration": 13,
        "Top_Speed": 105,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 55,
        "Length": 187,
        "Width": 69,
        "Height": 67,
        "Wheelbase": 110,
        "Cargo_Capacity": 25,
        "Seating_Capacity": 8,
        "Infotainment_System": "6-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS", "Lane Departure Warning"],
        "Interior_Features": ["Fabric seats", "Dual-zone climate control"],
        "Exterior_Features": ["Halogen headlights", "Alloy wheels"],
        "CO2_Emissions": 170,
        "Fuel_Efficiency_Rating": "C",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 18% per year",
        "Image": "https://example.com/toyota_noah.jpg"
    },
    {
        "id":14,
        "Name": "Toyota Hiace",
        "Kilometers_per_Liter": 10.5,
        "Miles_per_Gallon": 24.7,
        "Cylinders": 4,
        "Displacement": "2.5L",
        "Horsepower": "101 - 134",
        "Torque": "230 - 260",
        "Weight_in_lbs": 4500,
        "Acceleration": 15,
        "Top_Speed": 100,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic",
        "Drive_Type": "RWD",
        "Fuel_Type": "Diesel",
        "Fuel_Tank_Capacity": 70,
        "Length": 195,
        "Width": 75,
        "Height": 83,
        "Wheelbase": 123,
        "Cargo_Capacity": 30,
        "Seating_Capacity": 15,
        "Infotainment_System": "5-inch display",
        "Safety_Features": ["Airbags", "ABS"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 220,
        "Fuel_Efficiency_Rating": "D",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 15% per year",
        "Image": "https://example.com/toyota_hiace.jpg"
    },
    {
        "id":15,
        "Name": "Mitsubishi Canter",
        "Kilometers_per_Liter": 8.0,
        "Miles_per_Gallon": 18.8,
        "Cylinders": 4,
        "Displacement": "3.0L - 4.2L",
        "Horsepower": "150 - 175",
        "Torque": "280 - 320",
        "Weight_in_lbs": 6000,
        "Acceleration": 20,
        "Top_Speed": 90,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Manual",
        "Drive_Type": "RWD",
        "Fuel_Type": "Diesel",
        "Fuel_Tank_Capacity": 100,
        "Length": 224,
        "Width": 82,
        "Height": 93,
        "Wheelbase": 150,
        "Cargo_Capacity": 500,
        "Seating_Capacity": 3,
        "Infotainment_System": "None",
        "Safety_Features": ["Airbags (Optional)", "ABS"],
        "Interior_Features": ["Vinyl seats"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 300,
        "Fuel_Efficiency_Rating": "E",
        "Warranty": "1 year/unlimited miles",
        "Maintenance_Schedule": "Oil change every 7,500 miles",
        "Resale_Value": "Depreciates 25% per year",
        "Image": "https://example.com/mitsubishi_canter.jpg"
    },
    {
        "id":16,
        "Name": "Nissan B14 (Nissan Sunny)",
        "Kilometers_per_Liter": 14.0,
        "Miles_per_Gallon": 32.9,
        "Cylinders": 4,
        "Displacement": "1.3L - 1.5L",
        "Horsepower": "85 - 100",
        "Torque": "100 - 120",
        "Weight_in_lbs": 2200,
        "Acceleration": 13,
        "Top_Speed": 105,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic/Manual",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 40,
        "Length": 170,
        "Width": 66,
        "Height": 56,
        "Wheelbase": 102,
        "Cargo_Capacity": 10,
        "Seating_Capacity": 5,
        "Infotainment_System": "3-inch display (Basic radio)",
        "Safety_Features": ["Airbags (Optional)", "ABS (Optional)"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 150,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "2 years/24,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image": "https://example.com/nissan_b14.jpg"
    },
    {
        "id":17,
        "Name": "Mazda CX-5",
        "Kilometers_per_Liter": 14.5,
        "Miles_per_Gallon": 34.1,
        "Cylinders": 4,
        "Displacement": "2.0L - 2.5L",
        "Horsepower": "155 - 250",
        "Torque": "150 - 310",
        "Weight_in_lbs": 3500,
        "Acceleration": 8.5,
        "Top_Speed": 130,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic",
        "Drive_Type": "AWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 56,
        "Length": 179,
        "Width": 72,
        "Height": 66,
        "Wheelbase": 106,
        "Cargo_Capacity": 31,
        "Seating_Capacity": 5,
        "Infotainment_System": "8-inch touchscreen with Apple CarPlay/Android Auto",
        "Safety_Features": ["Airbags", "ABS", "Blind Spot Monitoring"],
        "Interior_Features": ["Leather seats", "Dual-zone automatic climate control"],
        "Exterior_Features": ["LED headlights", "Alloy wheels"],
        "CO2_Emissions": 150,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image": "https://example.com/mazda_cx5.jpg"
    },
    {
        "id":18,
        "Name": "Subaru Impreza",
        "Kilometers_per_Liter": 12.5,
        "Miles_per_Gallon": 29.4,
        "Cylinders": 4,
        "Displacement": "2.0L",
        "Horsepower": "152 - 310",
        "Torque": "145 - 290",
        "Weight_in_lbs": 3000,
        "Acceleration": 8,
        "Top_Speed": 125,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "CVT",
        "Drive_Type": "AWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 50,
        "Length": 177,
        "Width": 71,
        "Height": 57,
        "Wheelbase": 105,
        "Cargo_Capacity": 12,
        "Seating_Capacity": 5,
        "Infotainment_System": "6.5-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS", "EyeSight Driver Assist"],
        "Interior_Features": ["Fabric seats", "Automatic climate control"],
        "Exterior_Features": ["LED headlights", "Alloy wheels"],
        "CO2_Emissions": 160,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 6,000 miles",
        "Resale_Value": "Depreciates 18% per year",
        "Image": "https://example.com/subaru_impreza.jpg"
    },

    {
        "id":19,
        "Name": "Toyota March",
        "Kilometers_per_Liter": 18.5,
        "Miles_per_Gallon": 43.5,
        "Cylinders": 3,
        "Displacement": "1.0L",
        "Horsepower": 69,
        "Torque": 95,
        "Weight_in_lbs": 1800,
        "Acceleration": 10,
        "Top_Speed": 110,
        "Year": "2018-01-01",
        "Origin": "Japan",
        "Transmission": "CVT",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 35,
        "Length": 153,
        "Width": 67,
        "Height": 60,
        "Wheelbase": 98,
        "Cargo_Capacity": 10,
        "Seating_Capacity": 5,
        "Infotainment_System": "6-inch touchscreen",
        "Safety_Features": ["Airbags", "ABS"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Steel wheels"],
        "CO2_Emissions": 120,
        "Fuel_Efficiency_Rating": "A",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 20% per year",
        "Image": "https://example.com/toyota_march.jpg"
    },
    {
        "id":20,
        "Name": "Volkswagen Polo",
        "Kilometers_per_Liter": 18.0,
        "Miles_per_Gallon": 42.3,
        "Cylinders": 4,
        "Displacement": "1.0L - 1.6L",
        "Horsepower": "80 - 120",
        "Torque": "95 - 150",
        "Weight_in_lbs": 2600,
        "Acceleration": 10,
        "Top_Speed": 120,
        "Year": "2022-01-01",
        "Origin": "Germany",
        "Transmission": "Automatic/Manual",
        "Drive_Type": "FWD",
        "Fuel_Type": "Petrol",
        "Fuel_Tank_Capacity": 45,
        "Length": 160,
        "Width": 68,
        "Height": 56,
        "Wheelbase": 98,
        "Cargo_Capacity": 12,
        "Seating_Capacity": 5,
        "Infotainment_System": "8-inch touchscreen with Apple CarPlay/Android Auto",
        "Safety_Features": ["Airbags", "ABS", "ESC"],
        "Interior_Features": ["Fabric seats", "Manual air conditioning"],
        "Exterior_Features": ["Halogen headlights", "Alloy wheels"],
        "CO2_Emissions": 130,
        "Fuel_Efficiency_Rating": "B",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 5,000 miles",
        "Resale_Value": "Depreciates 15% per year",
        "Image": "https://example.com/volkswagen_polo.jpg"
    },
    {
        "id":21,
        "Name": "Mazda CX-5 Diesel",
        "Kilometers_per_Liter": 15.0,
        "Miles_per_Gallon": 35.3,
        "Cylinders": 4,
        "Displacement": "2.2L",
        "Horsepower": "173 - 184",
        "Torque": "310 - 325",
        "Weight_in_lbs": 3500,
        "Acceleration": 8.5,
        "Top_Speed": 130,
        "Year": "2022-01-01",
        "Origin": "Japan",
        "Transmission": "Automatic",
        "Drive_Type": "AWD",
        "Fuel_Type": "Diesel",
        "Fuel_Tank_Capacity": 56,
        "Length": 179,
        "Width": 73,
        "Height": 67,
        "Wheelbase": 106,
        "Cargo_Capacity": 30,
        "Seating_Capacity": 5,
        "Infotainment_System": "8-inch touchscreen with Apple CarPlay/Android Auto",
        "Safety_Features": ["Airbags", "ABS", "Lane Keep Assist"],
        "Interior_Features": ["Leather seats", "Dual-zone climate control"],
        "Exterior_Features": ["LED headlights", "Alloy wheels"],
        "CO2_Emissions": 120,
        "Fuel_Efficiency_Rating": "A",
        "Warranty": "3 years/36,000 miles",
        "Maintenance_Schedule": "Oil change every 7,500 miles",
        "Resale_Value": "Depreciates 18% per year",
        "Image": "https://example.com/mazda_cx5_diesel.jpg"
    }  
]

@app.get("/")
def get_messo():
    return {"message" : {"there are only two links for now"}, "links" : {"link/cars and link/cars/id_of_car"}, "more info" : {"only a few vehicles are available for now"}}

@app.get("/cars")
def get_cars(): # type: ignore
    return {"cars":my_cars}

@app.get("/cars/{id}")
def get_car(id: int):
    car = find_car(id)
    
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    return {"car": car}

@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_car(car: Car, id: int):
    car_dict = car.model_dump()
    
    
    car_dict['id'] = range(0,100000)
    
    my_cars.append(car_dict)
    return{"message": car_dict}