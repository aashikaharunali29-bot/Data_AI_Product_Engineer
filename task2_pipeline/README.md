# Task 2 - Weather Data Pipeline

## Objective

Build a simple data pipeline using an external API, transform the data, and load it into BigQuery.

## API Used

Open-Meteo API

## Workflow

1. Fetch weather data from API
2. Transform response into structured format
3. Add derived field (`weather_score`)
4. Save data to CSV
5. Upload CSV into BigQuery
6. Run SQL query

## Files

- `weather_pipeline.py` → Main pipeline code
- `weather_data.csv` → Generated dataset
- `sql_query.sql` → SQL query
- `screenshots/` → BigQuery screenshot

## Output Example

Generated fields:

- city
- temperature
- humidity
- wind_speed
- weather_score

## Improvements for Production

Future improvements:

- Scheduled execution
- Logging monitoring
- Error alerts
- Cloud deployment