const compliments = [
    "You're the heart of our home ❤️",
    "Thank you for your endless love 🌼",
    "You're my role model and best friend 🌟",
    "Your hugs heal everything 🤗",
    "You're stronger than you know 💪",
  ];
  
  function showCompliment() {
    const message = document.getElementById("message");
    const randomIndex = Math.floor(Math.random() * compliments.length);
    message.textContent = compliments[randomIndex];
  }
  
  function showSurprise() {
    const surprise = document.getElementById("surprise");
    surprise.classList.toggle("hidden");
  }
  