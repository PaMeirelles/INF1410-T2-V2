"use strict";
onload = function () {
    exibeLista();
};
function exibeLista() {
    fetch(backendAddress + "api/lista/")
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
                const postLink = document.createElement('a');
                postLink.href = 'post_detail.html/' + post.id;
                postLink.textContent = post.titulo;
                postElement.innerHTML = `
                        <h1>${postLink.outerHTML}</h1>
                        <p>${post.corpo}</p>
                        <p>Publicado em ${post.dt_publicado} por ${post.autor}</p>
                    `;
                postListElement.appendChild(postElement);
            }
        }
        else {
            console.error('Element with id "post-list" not found');
        }
    });
}
