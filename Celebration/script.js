const compliments = [
    "You're always sacrificing for us ❤️",
    "Thank you for your endless love and help 🌼",
    "You're my role model and best friend 🌟",
    "Your cooking is unreplacable 🤗",
    "You're stronger than everyone, even Papa 💪",
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
  
