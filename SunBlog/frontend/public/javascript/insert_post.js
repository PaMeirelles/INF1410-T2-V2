"use strict";
function submitForm() {
    var _a, _b;
    const titulo = (_a = document.getElementById('titulo')) === null || _a === void 0 ? void 0 : _a.getAttribute("value");
    const corpo = (_b = document.getElementById('corpo')) === null || _b === void 0 ? void 0 : _b.getAttribute("value");
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
