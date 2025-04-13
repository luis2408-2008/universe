// Gallery functionality for the cosmic image gallery
document.addEventListener('DOMContentLoaded', function() {
    initializeGallery();
});

function initializeGallery() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    if (galleryItems.length === 0) return;
    
    // Add click listeners to gallery items
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const imgSrc = this.querySelector('img').src;
            const imgTitle = this.querySelector('.gallery-title').textContent;
            const imgDesc = this.querySelector('.gallery-desc').textContent;
            const imgSource = this.querySelector('.gallery-source').textContent;
            
            openLightbox(imgSrc, imgTitle, imgDesc, imgSource);
        });
    });
    
    // Create lightbox if it doesn't exist
    if (!document.getElementById('cosmic-lightbox')) {
        createLightbox();
    }
}

function createLightbox() {
    const lightbox = document.createElement('div');
    lightbox.id = 'cosmic-lightbox';
    lightbox.className = 'fixed inset-0 bg-black bg-opacity-90 z-50 hidden flex items-center justify-center';
    
    const content = `
        <div class="lightbox-content max-w-4xl w-full mx-auto p-4">
            <button id="close-lightbox" class="absolute top-4 right-4 text-white text-2xl">&times;</button>
            <div class="lightbox-image-container mb-4">
                <img id="lightbox-image" class="max-h-[70vh] mx-auto" src="" alt="">
            </div>
            <div class="lightbox-info bg-gray-900 bg-opacity-80 p-4 rounded-lg">
                <h3 id="lightbox-title" class="text-xl font-bold text-purple-300 mb-2"></h3>
                <p id="lightbox-desc" class="text-gray-200 mb-2"></p>
                <p class="text-sm text-gray-400">Fuente: <span id="lightbox-source"></span></p>
            </div>
        </div>
    `;
    
    lightbox.innerHTML = content;
    document.body.appendChild(lightbox);
    
    // Add event listeners for lightbox
    document.getElementById('close-lightbox').addEventListener('click', closeLightbox);
    
    // Close lightbox when clicking outside the image
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });
    
    // Close lightbox with escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeLightbox();
        }
    });
}

function openLightbox(imgSrc, title, description, source) {
    const lightbox = document.getElementById('cosmic-lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxTitle = document.getElementById('lightbox-title');
    const lightboxDesc = document.getElementById('lightbox-desc');
    const lightboxSource = document.getElementById('lightbox-source');
    
    // Set lightbox content
    lightboxImage.src = imgSrc;
    lightboxTitle.textContent = title;
    lightboxDesc.textContent = description;
    lightboxSource.textContent = source;
    
    // Show lightbox with a fade-in effect
    lightbox.classList.remove('hidden');
    
    // Prevent body scrolling when lightbox is open
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    const lightbox = document.getElementById('cosmic-lightbox');
    
    lightbox.classList.add('hidden');
    
    // Re-enable body scrolling
    document.body.style.overflow = '';
}

// Add masonry layout to gallery
function initializeMasonryLayout() {
    const gallery = document.querySelector('.gallery-container');
    
    if (!gallery) return;
    
    // Check if imagesLoaded and Masonry are available
    if (typeof imagesLoaded !== 'undefined' && typeof Masonry !== 'undefined') {
        imagesLoaded(gallery, function() {
            new Masonry(gallery, {
                itemSelector: '.gallery-item',
                columnWidth: '.gallery-item',
                percentPosition: true
            });
        });
    } else {
        console.log('Masonry layout not available, using CSS grid instead');
    }
}

// Initialize filtering functionality for gallery
function initializeGalleryFilters() {
    const filterButtons = document.querySelectorAll('.gallery-filter');
    
    if (filterButtons.length === 0) return;
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Filter gallery items
            const galleryItems = document.querySelectorAll('.gallery-item');
            
            galleryItems.forEach(item => {
                if (filterValue === 'all') {
                    item.style.display = 'block';
                } else {
                    const category = item.getAttribute('data-category');
                    if (category === filterValue) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                }
            });
            
            // Reinitialize masonry layout if available
            if (typeof Masonry !== 'undefined') {
                setTimeout(initializeMasonryLayout, 300);
            }
        });
    });
}
