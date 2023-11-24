"use strict";
onload = function () {
    exibeLista();
};
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
