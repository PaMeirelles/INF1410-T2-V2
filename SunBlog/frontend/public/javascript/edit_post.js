"use strict";
// Function to submit the form
function saveForm() {
    var _a, _b;
    const pathParts = window.location.pathname.split('/');
    const id = pathParts[pathParts.length - 2];
    const titulo = (_a = document.getElementById('titulo')) === null || _a === void 0 ? void 0 : _a.getAttribute("value");
    const corpo = (_b = document.getElementById('corpo')) === null || _b === void 0 ? void 0 : _b.getAttribute("value");
    const postData = {
        titulo: titulo,
        corpo: corpo,
    };
    const token = localStorage.getItem('token');
    console.log("tititit" + titulo);
    fetch(backendAddress + 'api/umpost/' + id + '/', {
        method: 'PUT', // Assuming you are updating the post with a PUT request
        headers: {
            'Authorization': 'token ' + token,
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,
        },
        body: JSON.stringify(postData),
    })
        .then(response => {
        if (!response.ok) {
            throw new Error(`Failed to update post. API responded with ${response.status} status.`);
        }
        return response.json();
    })
        .then(data => {
        // Handle success, e.g., redirect to the blog post page
        console.log('Post updated successfully:', data);
        window.location.replace('/blog/posts/');
    })
        .catch(error => {
        // Handle error, e.g., display an error message
        console.error(error);
        alert(error.message || 'An error occurred.');
    });
}
// Function to delete the post
function deletePost() {
    const pathParts = window.location.pathname.split('/');
    const id = pathParts[pathParts.length - 2];
    if (confirm('Are you sure you want to delete this post?')) {
        const token = localStorage.getItem('token');
        fetch(backendAddress + 'api/umpost/' + id + '/', {
            method: 'DELETE',
            headers: {
                'Authorization': 'token ' + token,
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,
            },
        })
            .then(data => {
            // Handle success, e.g., redirect to the blog post page
            console.log('Post deleted successfully:', data);
            window.location.replace('/blog/posts/');
        })
            .catch(error => {
            // Handle error, e.g., display an error message
            console.error(error);
            alert(error.message || 'An error occurred.');
        });
    }
}
