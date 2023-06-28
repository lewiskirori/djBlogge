// header.js

(function() {
    function setGreeting() {
      var hour = new Date().getHours();
      var greeting = '';
      var username = '{{ request.user.username|default:"User"|lower }}';
    
      if (hour < 12) {
        greeting = 'Good Morning';
      } else if (hour < 16) {
        greeting = 'Good Afternoon';
      } else if (hour < 22) {
        greeting = 'Good Evening';
      } else {
        greeting = 'Good Night';
      }
    
      var greetingElem;
    
      if (greeting === 'Good Morning') {
        greetingElem = document.querySelector('.Morning-User');
      } else if (greeting === 'Good Afternoon') {
        greetingElem = document.querySelector('.Noon-User');
      } else if (greeting === 'Good Evening') {
        greetingElem = document.querySelector('.Evening-User');
      } else {
        greetingElem = document.querySelector('.Night-User');
      }
    
      if (greetingElem) {
        greetingElem.textContent = username;
      }
    }
    
    function handleLogout() {
      var logoutButton = document.querySelector('#logout-button');
    
      logoutButton.addEventListener('click', function() {
        logoutButton.disabled = true;
        logoutButton.innerHTML = '<i class="spinner-border spinner-border-sm"></i> Logging out...';
    
        setTimeout(function() {
          document.getElementById('logout-form').submit();
        }, 2000);
      });
    }
    
    function handleSearchOverlay() {
      var searchIcon = document.querySelector('.search-icon');
      var searchOverlay = document.querySelector('.search-overlay');
      var closeButton = document.querySelector('.close-button');
      var searchInput = document.querySelector('.search-form input[type="text"]');
      var searchButton = document.querySelector('.search-button');
    
      searchIcon.addEventListener('click', function() {
        searchOverlay.style.display = 'block';
        searchInput.focus();
    
        searchOverlay.addEventListener('click', function(event) {
          if (event.target === searchOverlay) {
            searchOverlay.style.transition = 'opacity 0.3s ease';
            searchOverlay.style.opacity = '0';
    
            setTimeout(function() {
              searchOverlay.style.display = 'none';
              searchOverlay.style.opacity = '1';
              searchOverlay.style.transition = 'none';
            }, 300);
          }
        });
      });
    
      closeButton.addEventListener('click', function() {
        searchOverlay.style.display = 'none';
        searchInput.value = '';
      });
    
      searchInput.addEventListener('input', function() {
        if (searchInput.value.length > 0) {
          closeButton.style.display = 'block';
        } else {
          closeButton.style.display = 'none';
        }
      });
    
      searchButton.addEventListener('click', function() {
        var form = document.querySelector('.search-form');
        form.submit();
      });
    }
    
    setGreeting();
    handleLogout();
    handleSearchOverlay();
  })();
  