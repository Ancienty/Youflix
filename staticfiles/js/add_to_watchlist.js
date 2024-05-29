document.addEventListener('DOMContentLoaded', () => {
    const addToWatchlistButtons = document.querySelectorAll('.add-to-watchlist');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    addToWatchlistButtons.forEach(button => {
        button.addEventListener('click', () => {
            console.log('Button clicked'); 

            const movieId = button.dataset.movieId;
            console.log('Movie ID:', movieId); 

            fetch(addToWatchlistUrl, {
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
                    button.textContent = 'Added to Watchlist';
                    button.disabled = true;
                } else {
                    console.error('Failed to add to watchlist:', data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
