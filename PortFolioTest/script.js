// Theme Toggle
document.getElementById('theme-button').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const themeButton = document.getElementById('theme-button');
    themeButton.textContent = document.body.classList.contains('dark-mode') ? '🌙' : '🌞';
});
