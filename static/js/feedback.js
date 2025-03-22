document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        try {
            const response = await fetch(form.action, {
                method: form.method,
                body: new FormData(this),
            });
            
            const data = await response.json();
            console.log(data);
            
            if (data.success) {
                alert(data.message);
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
        
        // Hide the original submit button
        const submitButton = document.querySelector('button[type="submit"]');
        if (submitButton) {
            submitButton.style.display = 'none';
        }
        
        // Wait for 5 seconds before removing the feedback
        setTimeout(() => {
            feedbackDiv.remove();
            if (submitButton) {
                submitButton.style.display = '';
            }
        }, 5000);
    }
});