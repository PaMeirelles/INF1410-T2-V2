"use strict";
function submitForm() {
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
            'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,
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
        console.log("batata");
        window.location.replace('/blog/posts');
    })
        .catch(error => {
        // Handle error, e.g., display an error message
        console.error(error);
        alert(error.message || 'An error occurred.');
    });
}
