document.addEventListener('DOMContentLoaded', () => {
    alert('JavaScript file is loaded'); 

    const removeFromWatchlistButtons = document.querySelectorAll('.remove-from-watchlist');
    console.log(`Found ${removeFromWatchlistButtons.length} remove buttons`); 

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log('CSRF Token:', csrfToken); 

    removeFromWatchlistButtons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Button clicked'); 

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
