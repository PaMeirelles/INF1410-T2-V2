"use strict";

// Function to submit the form
function saveForm() {
  const pathParts = window.location.pathname.split('/');
  const id = pathParts[pathParts.length - 2];
  const titulo = document.getElementById('titulo')?.value;
  const corpo = document.getElementById('corpo')?.value;

  const postData = {
    titulo: titulo,
    corpo: corpo,
  };

  const token = localStorage.getItem('token');
  
  fetch(backendAddress + 'api/umpost/' + id + '/', {
    method: 'PUT', // Assuming you are updating the post with a PUT request
    headers: {
      'Authorization': 'token ' + token,
      'Content-Type': 'application/json',
      'X-CSRFToken': (document.querySelector('input[name="csrfmiddlewaretoken"]') as HTMLInputElement)?.value,
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
        'X-CSRFToken': (document.querySelector('input[name="csrfmiddlewaretoken"]') as HTMLInputElement)?.value,
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
