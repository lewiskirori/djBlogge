// base.js

// Color theme
function toggleTheme() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.toggle("dark-mode");
  
    var button = document.querySelector(".theme-button");
    var sun = document.querySelector(".fa-moon");
    var moon = document.querySelector(".fa-sun");
  
    if (body.classList.contains("dark-mode")) {
      sun.style.display = "none";
      moon.style.display = "inline-block";
      invertFontColor("dark");
      localStorage.setItem("theme", "dark");
    } else {
      moon.style.display = "none";
      sun.style.display = "inline-block";
      invertFontColor("light");
      localStorage.setItem("theme", "light");
    }
  }
  
  function invertFontColor(theme) {
    var elements = document.querySelectorAll(".invert-color");
    for (var i = 0; i < elements.length; i++) {
      if (theme === "dark") {
        elements[i].style.color = "#f5f5f5";
      } else {
        elements[i].style.color = "#000";
      }
    }
  }
  
  // Check for theme preference on load
  var theme = localStorage.getItem("theme");
  if (theme === "dark") {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("dark-mode");
    var button = document.querySelector(".theme-button");
    var sun = document.querySelector(".fa-moon");
    var moon = document.querySelector(".fa-sun");
    sun.style.display = "none";
    moon.style.display = "inline-block";
    invertFontColor("dark");
  }
  
  // Page loader
  document.addEventListener("DOMContentLoaded", () => {
    const preloader = document.querySelector("#preloader");
    if (preloader) {
      preloader.classList.add("hide");
      setTimeout(() => {
        preloader.remove();
      }, 1000);
    }
  });
  
  // Scroll top
  var backToTopBtn = document.querySelector(".back-to-top-btn");
  
  window.addEventListener("scroll", function() {
    if (window.pageYOffset > 300) {
      backToTopBtn.classList.add("show");
    } else {
      backToTopBtn.classList.remove("show");
    }
  });
  
  backToTopBtn.addEventListener("click", function() {
    scrollTop(1000);
  });
  
  function scrollTop(duration) {
    var position = window.pageYOffset;
    var startingTime = null;
  
    function animation(currentTime) {
      if (startingTime === null) startingTime = currentTime;
      var timeElapsed = currentTime - startingTime;
      var run = ease(timeElapsed, position, -position, duration);
      window.scrollTo(0, run);
      if (timeElapsed < duration) requestAnimationFrame(animation);
    }
  
    function ease(t, b, c, d) {
      t /= d / 2;
      if (t < 1) return c / 2 * t * t + b;
      t--;
      return -c / 2 * (t * (t - 2) - 1) + b;
    }
  
    requestAnimationFrame(animation);
  }
  
  tippy('[data-tippy-content]', {
    arrow: false,
    theme: 'twitter',
    placement: 'bottom',
  });
  