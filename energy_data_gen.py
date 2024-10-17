import pandas as pd
import numpy as np

np.random.seed(42)

num_buildings = 10
building_ids = [f"B{str(i).zfill(3)}" for i in range(1, num_buildings + 1)]

months = (
    pd.date_range(start="2023-01-01", periods=12, freq="ME").strftime("%Y-%m").tolist()
)

# energy_usage.csv
energy_usage_data = []
for building_id in building_ids:
    for month in months:
        electricity_usage = np.random.uniform(1000, 5000)  # kWh
        gas_usage = np.random.uniform(200, 1000)  # cubic meters
        water_usage = np.random.uniform(500, 2000)  # liters
        total_energy_cost = (
            (electricity_usage * 0.15) + (gas_usage * 0.06) + (water_usage * 0.001)
        )
        energy_usage_data.append(
            [
                building_id,
                month,
                electricity_usage,
                gas_usage,
                water_usage,
                total_energy_cost,
            ]
        )

energy_usage_df = pd.DataFrame(
    energy_usage_data,
    columns=[
        "building_id",
        "month",
        "electricity_usage_kwh",
        "gas_usage_m3",
        "water_usage_l",
        "total_energy_cost_eur",
    ],
)

# building_specs.csv
building_specs_data = []
locations = ["CityA", "CityB", "CityC", "CityD", "CityE"]
building_types = ["Residential", "Commercial", "Industrial"]
for building_id in building_ids:
    location = np.random.choice(locations)
    building_size = np.random.uniform(500, 5000)  # m2
    occupants = np.random.randint(5, 200)
    year_built = np.random.randint(1980, 2022)
    building_type = np.random.choice(building_types)
    insulation_rating = np.random.randint(1, 5)  # Scale 1-5
    solar_panels = np.random.choice([True, False])
    heating_type = np.random.choice(["Gas", "Electric", "Solar"])
    building_specs_data.append(
        [
            building_id,
            location,
            building_size,
            occupants,
            year_built,
            building_type,
            insulation_rating,
            solar_panels,
            heating_type,
        ]
    )

building_specs_df = pd.DataFrame(
    building_specs_data,
    columns=[
        "building_id",
        "location",
        "building_size_m2",
        "occupants",
        "year_built",
        "building_type",
        "insulation_rating",
        "solar_panels",
        "heating_type",
    ],
)

# weather.csv
weather_data = []
for location in locations:
    for month in months:
        avg_temperature = np.random.uniform(-5, 35)  # Celsius
        precipitation = np.random.uniform(0, 100)  # mm
        humidity = np.random.uniform(30, 90)  # percentage
        solar_radiation = np.random.uniform(0, 10)  # kWh/m2
        weather_data.append(
            [location, month, avg_temperature, precipitation, humidity, solar_radiation]
        )

weather_df = pd.DataFrame(
    weather_data,
    columns=[
        "location",
        "month",
        "avg_temperature_celsius",
        "precipitation_mm",
        "humidity_percent",
        "solar_radiation_kwh_m2",
    ],
)

# Adjust energy usage for stronger correlation with weather

# Merge energy usage data with building specs to include location
merged_energy_data = pd.merge(
    energy_usage_df, building_specs_df[["building_id", "location"]], on="building_id"
)

# Merge resulting data with the weather data on location and month
merged_data = pd.merge(merged_energy_data, weather_df, on=["location", "month"])

# Increase electricity usage with temperature (e.g. higher electricity usage in hotter months due to AC usage)
merged_data["electricity_usage_kwh"] += (
    merged_data["avg_temperature_celsius"] * 10
) 

# Increase gas usage in colder months (e.g. higher gas usage for heating)
merged_data["gas_usage_m3"] += (
    20 - merged_data["avg_temperature_celsius"]
) * 5 

# Slight increase in water usage with higher humidity (e.g. humidity impacts water consumption patterns)
merged_data["water_usage_l"] += (
    merged_data["humidity_percent"] * 2
)

# Save to CSV files
adjusted_energy_usage_df = merged_data[
    [
        "building_id",
        "month",
        "electricity_usage_kwh",
        "gas_usage_m3",
        "water_usage_l",
        "total_energy_cost_eur",
        "location",
    ]
]
adjusted_energy_usage_df.to_csv("data/energy_usage.csv", index=False)
building_specs_df.to_csv("data/building_specs.csv", index=False) 
weather_df.to_csv("data/weather.csv", index=False) 

