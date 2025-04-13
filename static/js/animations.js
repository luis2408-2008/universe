// Cosmic background animations
document.addEventListener('DOMContentLoaded', function() {
    // Create animated star background
    createStarryBackground();
    
    // Initialize animations for elements with animation classes
    initializeAnimations();
    
    // Handle flash messages
    setupFlashMessages();
});

// Create a starry background with twinkling stars
function createStarryBackground() {
    const starsContainer = document.querySelector('.stars');
    if (!starsContainer) return;
    
    const numberOfStars = 200;
    
    for (let i = 0; i < numberOfStars; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        
        // Random position
        const x = Math.random() * 100;
        const y = Math.random() * 100;
        
        // Random size between 1 and 3 pixels
        const size = Math.random() * 2 + 1;
        
        // Random duration between 3 and 7 seconds
        const duration = Math.random() * 4 + 3;
        
        // Random opacity between 0.5 and 1
        const opacity = Math.random() * 0.5 + 0.5;
        
        star.style.left = `${x}%`;
        star.style.top = `${y}%`;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        star.style.setProperty('--duration', `${duration}s`);
        star.style.setProperty('--opacity', opacity);
        
        starsContainer.appendChild(star);
    }
}

// Initialize animations for elements with animation classes
function initializeAnimations() {
    // Animate elements with the fade-in class when they come into view
    const fadeElements = document.querySelectorAll('.fade-in');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    fadeElements.forEach(element => {
        observer.observe(element);
    });
    
    // Add floating animation to elements with float class
    const floatElements = document.querySelectorAll('.float');
    
    floatElements.forEach(element => {
        // Add a slight random delay to make animations less synchronized
        const delay = Math.random() * 2;
        element.style.animationDelay = `${delay}s`;
    });
}

// Handle flash messages and make them disappear after a few seconds
function setupFlashMessages() {
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(message => {
        // After animation is complete, remove the message
        setTimeout(() => {
            message.remove();
        }, 4000); // Match the fadeInOut animation duration
    });
}

// Add parallax effect to background elements
document.addEventListener('mousemove', function(e) {
    const parallaxElements = document.querySelectorAll('.parallax');
    
    const mouseX = e.clientX;
    const mouseY = e.clientY;
    
    parallaxElements.forEach(element => {
        const speed = element.getAttribute('data-speed') || 0.1;
        const x = (window.innerWidth - mouseX * speed) / 100;
        const y = (window.innerHeight - mouseY * speed) / 100;
        
        element.style.transform = `translateX(${x}px) translateY(${y}px)`;
    });
});

// Add reveal animation to section headers when scrolled into view
window.addEventListener('scroll', function() {
    const headers = document.querySelectorAll('.section-header');
    
    headers.forEach(header => {
        const headerPosition = header.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        
        if (headerPosition < screenPosition) {
            header.classList.add('revealed');
        }
    });
});
