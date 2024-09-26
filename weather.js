// weather.js
require('dotenv').config();
const axios = require('axios');
const fs = require('fs');

// Fetch weather data from the free weather API (open-meteo in this case)
async function fetchWeatherData() {
    const apiKey = process.env.WEATHER_API_KEY;
    const baseUrl = 'https://api.open-meteo.com/v1/forecast';
    const latitude = -25.7479; // Example coordinates for Pretoria
    const longitude = 28.2293;

    try {
        const response = await axios.get(`${baseUrl}?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m`);
        const weatherData = response.data;

        // Write data to a JSON file
        fs.writeFileSync('./data/weatherData.json', JSON.stringify(weatherData, null, 2));

        console.log("Weather data saved successfully.");
    } catch (error) {
        console.error("Error fetching weather data:", error);
    }
}

fetchWeatherData();
