window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    var logo = document.getElementById('logo');
    var distanceY = window.pageYOffset || document.documentElement.scrollTop;
  
    if (distanceY > 0) {
      navbar.classList.add('smaller');
      logo.classList.add('smaller');
    } else {
      navbar.classList.remove('smaller');
      logo.classList.remove('smaller');

    }
  });
  