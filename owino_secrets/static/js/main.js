console.log("✅ main.js loaded");

document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".slide");

  slides.forEach(slide => {
    const bg = slide.getAttribute("data-bg");
    if (bg) {
      slide.style.backgroundImage = `url('${bg}')`;
    }
  });

  let currentSlide = 0;

  setInterval(() => {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
  }, 5000);
});