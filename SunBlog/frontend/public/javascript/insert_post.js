"use strict";
function submitForm() {
    var _a;
    const titulo = document.getElementById('titulo').value;
    const corpo = document.getElementById('corpo').value;
    const postData = {
        titulo: titulo,
        corpo: corpo,
    };
    const token = localStorage.getItem('token');
    fetch(backendAddress + 'api/umpost/', {
        method: 'POST',
        headers: {
            'Authorization': 'token ' + token,
            'Content-Type': 'application/json',
            'X-CSRFToken': (_a = document.querySelector('input[name="csrfmiddlewaretoken"]')) === null || _a === void 0 ? void 0 : _a.value,
        },
        body: JSON.stringify(postData),
    })
        .then(response => {
        if (!response.ok) {
            throw new Error(`Failed to create post. API responded with ${response.status} status.`);
        }
        return response.json();
    })
        .then(data => {
        // Handle success, e.g., redirect to the blog post page
        window.location.replace('/public/blog_posts.html');
    })
        .catch(error => {
        // Handle error, e.g., display an error message
        console.error(error);
        alert(error.message || 'An error occurred.');
    });
}
