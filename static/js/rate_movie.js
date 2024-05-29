document.addEventListener('DOMContentLoaded', () => {
    const rateMovieButtons = document.querySelectorAll('.rate-movie');

    rateMovieButtons.forEach(button => {
        button.addEventListener('click', () => {
            const movieId = button.dataset.movieId;
            const rating = prompt("Please enter your rating (1-5):");

            if (rating >= 1 && rating <= 5) {
                fetch(rateMovieUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    },
                    body: JSON.stringify({ movie_id: movieId, rating: rating })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        button.textContent = `Change Rating (${rating})`;
                        alert("Thank you for rating!");
                    } else {
                        alert("Failed to rate the movie.");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            } else {
                alert("Invalid rating. Please enter a number between 1 and 5.");
            }
        });
    });
});
