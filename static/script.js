document.getElementById("getWeather").addEventListener("click", async function() {
    const city = document.getElementById("city").value;
    const country = document.getElementById("country").value;
    
    if (city === "" || country === "") {
      alert("Please enter both city and country.");
      return;
    }
  
    try {
      const response = await fetch(`/weather?city=${city}&country=${country}`);
      const data = await response.json();
  
      if (data.error) {
        alert("Could not fetch weather data. Please try again.");
      } else {
        displayWeather(data);
      }
    } catch (error) {
      alert("Error fetching data.");
    }
  });
  
  function displayWeather(data) {
    const weatherSection = document.getElementById("weatherDetails");
    weatherSection.classList.remove("hidden");
  
    document.getElementById("location").innerText = `Weather in ${data.location}`;
    document.getElementById("temperature").innerText = `Temperature: ${data.temperature}°C`;
    document.getElementById("weather").innerText = `Condition: ${data.weather}`;  
    const weatherIcon = document.getElementById("weatherIcon");
    weatherIcon.innerHTML = `<img src="${data.icon}" alt="Weather icon">`;
  }
  