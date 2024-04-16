document.addEventListener('DOMContentLoaded', function() {
    document.querySelector(".logo").addEventListener('click', function() {
        const targetElement = document.querySelector('.logo');
        if (targetElement) {
          window.scrollTo({ top: targetElement.getBoundingClientRect().top + window.pageYOffset, behavior: 'smooth' });
        }
    });
});