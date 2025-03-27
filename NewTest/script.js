// Smooth Scroll for Navbar Links
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href').substring(1);
    document.getElementById(targetId).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  });
});

// Highlight Navbar Links on Scroll
const sections = document.querySelectorAll('section');
const navbarLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
  let currentSection = "";
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (scrollY >= sectionTop - 200) {
      currentSection = section.getAttribute('id');
    }
  });

  navbarLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href').substring(1) === currentSection) {
      link.classList.add('active');
    }
  });
});

// Add hover effect on Project Cards
const projectCards = document.querySelectorAll('.project-card');

projectCards.forEach(card => {
  card.addEventListener('mouseenter', () => {
    card.style.transform = 'scale(1.05)';
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'scale(1)';
  });
});

// Optional: Button Click for Contact Section
const contactButton = document.querySelector('.contact-button');

contactButton.addEventListener('click', () => {
  window.location.href = 'mailto:your-email@example.com';
});

// Add a typewriter effect for Hero Section (Optional)
const heroText = document.querySelector('.hero-content p');
const textToType = 'Software Engineer | Web Developer | Tech Enthusiast';

let i = 0;
function typeWriter() {
  if (i < textToType.length) {
    heroText.innerHTML += textToType.charAt(i);
    i++;
    setTimeout(typeWriter, 100);
  }
}

window.onload = typeWriter;
