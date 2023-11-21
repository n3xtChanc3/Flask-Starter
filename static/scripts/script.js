// static/scripts/script.js

function changeBackground(color) {
    var body = document.body;

    if (color === 'white') {
        body.style.backgroundColor = '#ffffff';
    } else if (color === 'black') {
        body.style.backgroundColor = '#000000';
    } else {
        // For random color change as before
        var colors = ['#f4f4f4', '#e6f7ff', '#ffe6e6', '#ccffcc', '#ffd699'];
        var randomColor = colors[Math.floor(Math.random() * colors.length)];
        body.style.backgroundColor = randomColor;
    }

    // Display success message
    var successMessage = document.getElementById('success-message');
    successMessage.style.display = 'block';

    // Hide the message after a few seconds (e.g., 3 seconds)
    setTimeout(function() {
        successMessage.style.display = 'none';
    }, 3000);
}
