document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript file loaded'); 

    const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    if (!csrfTokenElement) {
        console.error('CSRF token not found');
        return;
    }
    const csrfToken = csrfTokenElement.value;
    console.log('CSRF Token:', csrfToken); 

    const removeFromWatchlistUrl = window.removeFromWatchlistUrl;
    if (!removeFromWatchlistUrl) {
        console.error('removeFromWatchlistUrl is not defined');
        return;
    }

    const removeFromWatchlistButtons = document.querySelectorAll('.remove-from-watchlist');
    console.log(`Found ${removeFromWatchlistButtons.length} remove buttons`); 

    removeFromWatchlistButtons.forEach(button => {
        button.addEventListener('click', () => {
            console.log('Button clicked'); 

            const movieId = button.dataset.movieId;
            console.log('Movie ID:', movieId); 

            fetch(removeFromWatchlistUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ movie_id: movieId })
            })
            .then(response => {
                console.log('Response received'); 
                return response.json();
            })
            .then(data => {
                console.log('Response data:', data); 
                if (data.status === 'success') {
                    button.closest('.movie-item').remove(); 
                } else {
                    console.error('Failed to remove from watchlist:', data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
