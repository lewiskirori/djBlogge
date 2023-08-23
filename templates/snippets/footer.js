// footer.js

(function() {
    var currentYear = new Date().getFullYear();
    var currentYearElem = document.getElementById('current_year');
    
    if (currentYear && currentYear >= 2020) {
      currentYearElem.textContent = currentYear;
    } else {
      currentYearElem.textContent = 'Present';
    }
  })();
  