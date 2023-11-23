"use strict";
onload = function () {
    exibeLista();
};
function exibeLista() {
    fetch(backendAddress + "blog/api/blog/posts/")
        .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
        .then(posts => {
        const postListElement = document.getElementById('blog-posts');
        if (postListElement) {
            for (const post of posts) {
                const postElement = document.createElement('div');
                postElement.className = 'post';
                postElement.innerHTML = `
                        <h2>${post.titulo}</h2>
                        <p>${post.corpo}</p>
                        <p>Publicado em ${post.dt_publicado} por ${post.autor}</p>
                    `;
                postListElement.appendChild(postElement);
            }
        }
        else {
            console.error('Element with id "post-list" not found');
        }
    })
        .catch(error => {
        console.error('An error occurred while fetching the posts:', error);
    });
}
