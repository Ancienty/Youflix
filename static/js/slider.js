document.addEventListener("DOMContentLoaded", function () {
    const movies = document.querySelectorAll(".movie-item");
    let startIndex = 0;
    const visibleCount = 5;

    function updateVisibility() {
        movies.forEach((movie, index) => {
            if (index >= startIndex && index < startIndex + visibleCount) {
                movie.style.display = "block";
            } else {
                movie.style.display = "none";
            }
        });
    }

    document.getElementById("next-btn").addEventListener("click", function () {
        if (startIndex + visibleCount < movies.length) {
            startIndex++;
            updateVisibility();
        }
    });

    document.getElementById("prev-btn").addEventListener("click", function () {
        if (startIndex > 0) {
            startIndex--;
            updateVisibility();
        }
    });

    updateVisibility();
});
