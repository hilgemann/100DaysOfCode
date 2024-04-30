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
});

function removeAccents(str) {
    return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

$(document).ready(function() {
    $.getJSON('sabores.json', function(data) {
        var produtos = data;
        
        function atualizarCards(filtro) {
            var html = '';
            $('#card-lists').empty(); // Limpa os cards existentes
            $.each(produtos, function(index, produto) {
                // Verifica se o nome do produto contém o filtro digitado
                if (
                    removeAccents(produto.nome.toLowerCase()).includes(removeAccents(filtro.toLowerCase())) ||
                    removeAccents(produto.tipo.toLowerCase()).includes(removeAccents(filtro.toLowerCase())) ||
                    removeAccents(produto.descricao.toLowerCase()).includes(removeAccents(filtro.toLowerCase()))
                ) {
                    html += '<div class="col-xl-3 col-lg-4 col-md-4 col-sm-6 mb-4 d-flex flex-column align-items-center justify-content-start">';
                    html += '<div class="card">';
                    html += '<img src="images/' + produto.imagem + '" class="card-img-top" alt="' + produto.nome + '">';
                    html += '<div class="card-body">';
                    html += '<h5 class="card-title">' + produto.nome + '</h5>';
                    html += '<p class="card-text">' + produto.descricao + '</p>';
                    html += '</div></div></div>';
                }
            });

            $('#card-lists').html(html); // Atualiza os cards filtrados
        }

        // Atualiza os cards ao digitar no campo de input
        $('#filter').on('input', function() {
            var filtro = $(this).val();
            atualizarCards(filtro);
        });

        // Mostra todos os cards ao carregar a página
        atualizarCards('');
    });
});