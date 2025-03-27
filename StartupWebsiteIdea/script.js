// Smooth scrolling for navigation
document.querySelectorAll("nav ul li a").forEach(link => {
    link.addEventListener("click", function(event) {
        event.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        target.scrollIntoView({ behavior: "smooth" });
    });
});

// Interactive Contact Form
document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    // Show message
    const message = document.getElementById("form-message");
    message.classList.remove("hidden");

    // Hide after 3 seconds
    setTimeout(() => {
        message.classList.add("hidden");
    }, 3000);

    // Clear form fields
    this.reset();
});

// Dynamic Testimonials (Example of User Interaction)
const testimonials = [
    '"This product changed the way I work! Highly recommend it." - Happy Customer',
    '"An amazing innovation! I use it daily." - Tech Enthusiast',
    '"Customer support was outstanding. Love this brand!" - Verified Buyer'
];

let index = 0;
function updateTestimonial() {
    document.querySelector("#testimonials blockquote").innerText = testimonials[index];
    index = (index + 1) % testimonials.length;
}
setInterval(updateTestimonial, 5000);
