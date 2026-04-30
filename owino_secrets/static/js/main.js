console.log("✅ main.js loaded");

document.addEventListener("DOMContentLoaded", () => {
  // Apply background images from data-bg
  const bgElements = document.querySelectorAll("[data-bg]");

  bgElements.forEach(el => {
    const bg = el.getAttribute("data-bg");
    if (bg) {
      el.style.backgroundImage = `url('${bg}')`;
    }
  });

  // Slider logic (only affects hero slides)
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  if (slides.length > 1) {
    setInterval(() => {
      slides[currentSlide].classList.remove("active");
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add("active");
    }, 5000);
  }
});