"use strict";
// Assuming you have some way to get the post ID in your JavaScript context
const urlParams = new URLSearchParams(window.location.search);
const postId = urlParams.get('id');
const editForm = document.getElementById('post-edit-form');
const deleteBtn = document.getElementById('deleteBtn');
const token = localStorage.getItem('token');
editForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    // Assuming you have a function to serialize the form data into a JSON object
    const formData = serializeFormData(editForm);
    try {
        const response = await fetch(`/api/posts/${postId}/`, {
            method: 'PUT',
            headers: {
                'Authorization': 'token ' + token,
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,
            },
            body: JSON.stringify(formData),
        });
        if (response.ok) {
            window.location.replace('/blog/posts');
        }
        else {
            // Handle error, maybe display error messages
            const data = await response.json();
            console.error(data);
        }
    }
    catch (error) {
        console.error('Error:', error);
    }
});
deleteBtn.addEventListener('click', async () => {
    if (confirm('Are you sure you want to delete this post?')) {
        try {
            const response = await fetch(`/api/posts/${postId}/`, {
                method: 'DELETE',
                headers: {
                    'Authorization': 'token ' + token,
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,
                },
            });
            if (response.ok) {
                window.location.replace('/blog/posts');
            }
            else {
                // Handle error, maybe display error messages
                const data = await response.json();
                console.error(data);
            }
        }
        catch (error) {
            console.error('Error:', error);
        }
    }
});
function serializeFormData(form) {
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value.toString();
    });
    return data;
}
