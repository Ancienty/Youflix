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
        case 'stats':
            fullUrl = baseUrl + '/stats/';
            break;
        case 'profile':
            fullUrl = baseUrl + '/profile/';
            break;
        default:
            // Handle invalid page names if needed
            fullUrl = baseUrl;
    }

    window.location.href = fullUrl;
}
