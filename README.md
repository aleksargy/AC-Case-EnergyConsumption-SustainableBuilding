# Energy Consumption Analysis for a Sustainable Building Project

## Case Study

A company focused on sustainable architecture is designing and managing energy-efficient buildings. However, some of their properties are underperforming in terms of energy savings, which has sparked concerns about inefficiencies in building management. Your team has been asked to analyse energy consumption patterns across multiple buildings to uncover inefficiencies, determine which properties need improvement, and propose actionable steps to optimise energy use while maintaining sustainability goals.

### Objective

Identify trends, correlations, and anomalies in energy consumption across the company's buildings. Make recommendations for improving energy efficiency, and communicate findings in a way that can inform business and building management strategies.

---

## Dataset Overview

1. **`energy_usage.csv`**  
   - **Columns**: `building_id`, `month`, `electricity_usage_kwh`, `gas_usage_m3`, `water_usage_l`, `total_energy_cost_eur`  
   - **Description**: Contains monthly energy usage for electricity (in kilowatt-hours), gas (in cubic meters), and water (in liters) across different buildings. It also includes the total energy cost per building for each month.

2. **`building_specs.csv`**  
   - **Columns**: `building_id`, `location`, `building_size_m2`, `occupants`, `year_built`, `building_type`, `insulation_rating`, `solar_panels`, `heating_type`  
   - **Description**: Provides details about each building, including its size (in square meters), number of occupants, type of building (e.g., residential, commercial), year of construction, insulation quality (rated on a scale), whether it has solar panels, and the type of heating system used.

3. **`weather.csv`**  
   - **Columns**: `location`, `month`, `avg_temperature_celsius`, `precipitation_mm`, `humidity_percent`, `solar_radiation_kwh_m2`  
   - **Description**: Monthly weather data for the locations where the buildings are located. Includes average temperature, precipitation, humidity, and solar radiation (which may influence energy usage, especially in buildings with solar panels).

---

## Key Guiding Questions

1. **Analysing Energy Efficiency**:
   - Which buildings have the highest energy consumption per square meter? Is this trend consistent across different types of energy (electricity, gas, water)?
   - How does the presence of solar panels and insulation ratings impact overall energy consumption? Are there any correlations between these features and energy savings?
   - Which buildings are the most and least cost-effective in terms of energy usage?

2. **Correlations with Weather Data**:
   - How do external factors like temperature, humidity, and solar radiation affect energy consumption across different buildings?
   - Can you identify any seasonal trends in energy usage? Do buildings in colder climates have consistently higher heating-related energy usage?

3. **Building Performance Insights**:
   - Which buildings are performing well in terms of energy efficiency, and what factors might be contributing to their success (e.g., solar panel usage, newer insulation, fewer occupants)?
   - Are there underperforming buildings that require immediate interventions (e.g., heating system upgrades, insulation improvements)?

4. **Actionable Recommendations**:
   - Based on your analysis, what specific changes or investments should the company make to improve energy efficiency (e.g., retrofitting certain buildings, installing more solar panels)?
   - How can energy consumption trends help inform future building designs or operational strategies?

---

## Possible Deliverables

1. **Energy Efficiency Score**: Develop a scoring metric that ranks each building based on energy consumption per square meter, adjusted for external factors like weather and building specifications.
2. **Visualisations**: Provide clear visualisations that highlight high and low energy consumption buildings, seasonal trends, and the impact of building features like insulation and solar panels. Possible charts could include:
   - A bar chart showing energy consumption per building and energy type.
   - A scatter plot correlating energy usage with building size, number of occupants, or insulation rating.
   - A line graph showing the monthly energy usage trends across different locations.
   
3. **Energy Savings Recommendations**: Based on your findings, outline recommendations to improve energy efficiency. These should include specific suggestions, like upgrading insulation or optimising heating systems, with projected energy savings.

---

## Optional Frontend/Tool Component

Your team could build a **Building Energy Dashboard**. This dashboard would allow company managers to:
- **Monitor energy usage in real-time**: View energy consumption per building, compare it to historical trends, and identify inefficiencies quickly.
- **Visualise impact of interventions**: Input potential improvements (e.g., adding solar panels, upgrading insulation), and see the predicted reduction in energy consumption.
- **Filter by weather conditions**: Analyse how weather fluctuations affect different buildings, helping the company prepare for seasonal adjustments in energy management.

---

## Expected Outcome

At the end of this assignment, your team will present your findings in a 10-minute presentation. Focus on:
- Explaining which buildings are underperforming and why.
- Demonstrating your analytical approach with visuals and metrics.
- Offering clear, actionable recommendations for improving energy efficiency.
- Optionally showcasing any dashboard or tool you’ve built that supports ongoing monitoring and optimisation.
