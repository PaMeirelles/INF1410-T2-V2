"use strict";

function submitForm() {
  const titulo: string = (document.getElementById('titulo') as HTMLInputElement).value;
  const corpo: string = (document.getElementById('corpo') as HTMLInputElement).value;

  const postData = {
    titulo: titulo,
    corpo: corpo,
  };

  const token: string | null = localStorage.getItem('token');

  fetch(backendAddress + 'api/umpost/', {
    method: 'POST',
    headers: {
      'Authorization': 'token ' + token,
      'Content-Type': 'application/json',
      'X-CSRFToken': (document.querySelector('input[name="csrfmiddlewaretoken"]') as HTMLInputElement)?.value,
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
