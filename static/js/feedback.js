document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const radioButtons = form.querySelectorAll('input[type="radio"]');
    
    radioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            // Do nothing when radio buttons are changed
        });
    });

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

    try {
        const formData = new FormData(this);
        const response = await fetch(form.action, {
                method: form.method,
                body: formData,
            })

            const data = await response.json();
            console.log(data);
            
            if (data.success) {
                alert(data.message);
            } else if (data.redirect) {
                window.location.href = data.redirect;
            } else {
                showFeedback(data.error || 'An unknown error occurred');
            }
        } catch (error) {
            console.error('Error:', error);
            showFeedback('An unexpected error occurred');
        }
    });

    function showFeedback(message) {
        // Create a temporary div to hold the feedback
        const feedbackDiv = document.createElement('div');
        feedbackDiv.className = 'feedback-message';
        feedbackDiv.textContent = message;
        
        // Append the feedback to the body
        document.body.appendChild(feedbackDiv);
        
        // Wait for 5 seconds before removing the feedback
        setTimeout(() => {
            feedbackDiv.remove();
        }, 5000);
    }
});