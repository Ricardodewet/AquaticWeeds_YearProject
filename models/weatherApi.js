// models/weatherApi.js
const axios = require('axios');

const getWeatherData = async (latitude, longitude) => {
    try {
        const response = await axios.get(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m`);
        return response.data;
    } catch (error) {
        console.error("Error fetching weather data", error);
        throw error;
    }
};

module.exports = { getWeatherData };
