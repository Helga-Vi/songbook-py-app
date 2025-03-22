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

            const contentType = response.headers.get('content-type');
            console.log('Content-Type:', contentType);

            const data = await response.text();
            console.log('Response Data:', data.substring(0, 200));

            if (!contentType || !contentType.includes('application/json')) {
                throw new Error('Invalid content type');
            }
            
            const parsedData = JSON.parse(data);
            console.log('Parsed Data:', parsedData);

            if (parsedData.success) {
                alert(parsedData.message);
            } else if (parsedData.error) {
                showFeedback(parsedData.error || 'Vi finner en ny sang til deg');
                setTimeout(() => {
                    window.location.href = '/';
                }, 5000);
            } else {
                showFeedback(data.error || 'An unknown error occurred');
            }
        } catch (error) {
            console.error('Error:', error);
            showFeedback('An unexpected error occurred. Please try again.');
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