document.addEventListener('DOMContentLoaded', function() {
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightbox-img');
  var lightboxClose = document.getElementById('lightbox-close');
  var photoGallery = document.querySelector('.photo-gallery');
  
  if (!lightbox || !photoGallery) return;
  
  // Open lightbox
  photoGallery.addEventListener('click', function(e) {
    if (e.target.tagName === 'IMG') {
      lightboxImg.src = e.target.src;
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  });
  
  // Close lightbox
  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }
  
  if (lightboxClose) {
    lightboxClose.addEventListener('click', closeLightbox);
  }
  
  if (lightbox) {
    lightbox.addEventListener('click', function(e) {
      if (e.target === lightbox) {
        closeLightbox();
      }
    });
  }
  
  // Close on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });
});
