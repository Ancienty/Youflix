function navigateTo(page) {
    const baseUrl = window.location.origin; 
    let fullUrl;

    switch (page) {
        case 'home':
            fullUrl = baseUrl + '/';
            break;
        case 'movies':
            fullUrl = baseUrl + '/movies/';
            break;
        case 'quizzes':
            fullUrl = baseUrl + '/quizzes/';
            break;
        case 'profile':
            fullUrl = baseUrl + '/profile/';
            break;
        default:
            
            fullUrl = baseUrl;
    }

    window.location.href = fullUrl;
}
