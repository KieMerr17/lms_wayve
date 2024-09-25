document.addEventListener('DOMContentLoaded', function() {
    const showSignupBtn = document.getElementById('show-signup');
    const showLoginBtn = document.getElementById('show-login');
    const formWrapper = document.querySelector('.form-wrapper');
    const loginContainer = document.querySelector('.login-container');

    // Function to adjust the height dynamically based on the active form
    function adjustContainerHeight(isSignup) {
        if (isSignup) {
            // Increase height before the flip animation starts
            loginContainer.style.height = '500px';
        } else {
            // Set height before the flip animation starts
            loginContainer.style.height = '329px';
        }
    }

    // Add event listener for flipping to signup form
    showSignupBtn.addEventListener('click', function(event) {
        event.preventDefault();
        // First, adjust the height before the flip
        adjustContainerHeight(true);
        
        // Flip after a short delay
        setTimeout(() => {
            formWrapper.classList.add('flipped');
        }, 50);
    });

    // Add event listener for flipping back to login form
    showLoginBtn.addEventListener('click', function(event) {
        event.preventDefault();
        // First, adjust the height before the flip
        adjustContainerHeight(false);
        
        // Flip after a short delay
        setTimeout(() => {
            formWrapper.classList.remove('flipped');
        }, 50);
    });

    // Set initial height
    adjustContainerHeight(false); // Login form is initially shown
});
