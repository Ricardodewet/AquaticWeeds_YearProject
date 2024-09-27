document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('damCanvas');
    const ctx = canvas.getContext('2d');

    // Function to draw the dam, current and predicted hyacinth positions
    function drawDamPrediction() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw dam (blue)
        ctx.fillStyle = "#00008B";
        ctx.beginPath();
        ctx.ellipse(200, 150, 180, 100, 0, 0, 2 * Math.PI);
        ctx.fill();

        // Draw current hyacinth position (green)
        ctx.fillStyle = "#32CD32";
        ctx.beginPath();
        ctx.ellipse(200, 150, 130, 80, 0, 0, 2 * Math.PI);
        ctx.fill();

        // Draw predicted hyacinth position (purple)
        ctx.fillStyle = "#9370DB";
        ctx.beginPath();
        ctx.ellipse(220, 150, 150, 70, 0, 0, 2 * Math.PI);
        ctx.fill();
    }

    drawDamPrediction();

    // Handle form submission for changing date and time
    const timeForm = document.getElementById('timeForm');
    timeForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const date = document.getElementById('predictionDate').value;
        const time = document.getElementById('predictionTime').value;

        if (date && time) {
            const timeDisplay = document.querySelector('.time-display');
            timeDisplay.textContent = `${time} - ${date}`;

            // Show alert for confirmation
            alert('Prediction date and time changed successfully!');

            // Simulate prediction change
            drawDamPrediction(); 
        }
    });

    // Simulated data updates
    document.getElementById('growth-value').textContent = "6% Decrease";
    document.getElementById('wind-speed').textContent = "7m/s";
    document.getElementById('wind-direction').textContent = "NW";
    document.getElementById('water-level').textContent = "89.5 million m³";
    document.getElementById('movement-status').textContent = "HIGH";
    document.getElementById('flood-gates-status').textContent = "CLOSED";
});
