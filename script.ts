const toggleButton = document.getElementById('toggleBtn') as HTMLButtonElement;
const moreInfo = document.getElementById('moreInfo') as HTMLDivElement;

let isVisible = false;

toggleButton.addEventListener('click', () => {
  isVisible = !isVisible;
  moreInfo.classList.toggle('hidden', !isVisible);
  toggleButton.textContent = isVisible ? 'Show Less' : 'Show More';
});
