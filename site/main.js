window.addEventListener('DOMContentLoaded', event => {
  var navbarShrink = function () {
      const navbarCollapsible = document.body.querySelector('#mainNav');
      if (!navbarCollapsible) {
          return;
      }
      if (window.scrollY === 0) {
          navbarCollapsible.classList.remove('navbar-shrink')
      } else {
          navbarCollapsible.classList.add('navbar-shrink')
      }

  };

  navbarShrink();

  document.addEventListener('scroll', navbarShrink);

  const mainNav = document.body.querySelector('#mainNav');
  if (mainNav) {
      new bootstrap.ScrollSpy(document.body, {
          target: '#mainNav',
          rootMargin: '0px 0px -40%',
      });
  };

  const navbarToggler = document.body.querySelector('.navbar-toggler');
  const responsiveNavItems = [].slice.call(
      document.querySelectorAll('#navbarResponsive .nav-link')
  );
  responsiveNavItems.map(function (responsiveNavItem) {
      responsiveNavItem.addEventListener('click', () => {
          if (window.getComputedStyle(navbarToggler).display !== 'none') {
              navbarToggler.click();
          }
      });
  });

  new SimpleLightbox({
      elements: '#portfolio a.portfolio-box'
  });

  
});

$(document).ready(function() {
  $.getJSON('sabores.json', function(data) {
    var products = data;
    var html = '';
    console.log(products);
    $.each(products, function(index, produto) {
      html += '<div class="col-lg-3 col-md-6 mb-4 d-flex flex-column align-items-center justify-content-start">';
      html += '<div class="card">';
      html += '<img src="images/' + produto.imagem + '" class="card-img-top" alt="' + produto.nome + '">';
      html += '<div class="card-body">';
      html += '<h5 class="card-title">' + produto.nome + '</h5>';
      html += '<p class="card-text">' + produto.descricao + '</p>';
      html += '</div></div></div>';
    });

    $('#card-lists').html(html);
  });
});

const flavorsHandle = function () {
  
}
