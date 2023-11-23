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
                const postLink = document.createElement('a');
                postLink.href = backendAddress + 'blog/post/' + post.id;
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
function exibeDetalhes(postId) {
    fetch(backendAddress + "blog/api/blog/post/" + postId)
        .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
        .then(post => {
        const postElement = document.getElementById('post-detail');
        if (postElement) {
            postElement.innerHTML = `
                    <h1>${post.titulo}</h1>
                    <p>${post.corpo}</p>
                    <p>Publicado em ${post.dt_publicado} por ${post.autor}</p>
                    <a href="/blog/posts/">Voltar para a lista de posts</a>
                `;
        }
        else {
            console.error('Element with id "post-detail" not found');
        }
    })
        .catch(error => {
        console.error('An error occurred while fetching the post:', error);
    });
}
