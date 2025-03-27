document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();
    document.getElementById("form-message").classList.remove("hidden");
    setTimeout(() => {
        document.getElementById("form-message").classList.add("hidden");
    }, 3000);
});

// Smooth scrolling for navigation links
document.querySelectorAll("nav ul li a").forEach(link => {
    link.addEventListener("click", function(event) {
        event.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        target.scrollIntoView({ behavior: "smooth" });
    });
});
