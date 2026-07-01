// Intersection Observer for scroll animations
document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add a small delay based on index for staggered animation
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all project showcases
    document.querySelectorAll('.project-showcase').forEach(showcase => {
        observer.observe(showcase);
    });

    // Parallax effect for blobs
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const blob1 = document.querySelector('.blob-1');
        const blob2 = document.querySelector('.blob-2');
        
        if(blob1) blob1.style.transform = `translateY(${scrolled * 0.2}px)`;
        if(blob2) blob2.style.transform = `translateY(-${scrolled * 0.1}px)`;
    });
});
