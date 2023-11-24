"use strict";
function exibeDetalhes(postId) {
    fetch(backendAddress + "blog/api/blog/post/" + postId)
        .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
        .then(post => {
        var _a;
        const postElement = document.getElementById('post-detail');
        const userId = (_a = document.getElementById('userId')) === null || _a === void 0 ? void 0 : _a.getAttribute("value");
        console.log(userId);
        console.log(post.autor);
        if (postElement) {
            let html = `
                    <h1>${post.titulo}</h1>
                    <p>${post.corpo}</p>
                    <p>Publicado em ${post.dt_publicado} por ${post.autor}</p>
                    <a href="/blog/posts/">Voltar para a lista de posts</a>
                `;
            if (post.autor == userId) {
                html += `<a href="/blog/edit_post/${post.id}/">Editar este post</a>`;
            }
            postElement.innerHTML = html;
        }
        else {
            console.error('Element with id "post-detail" not found');
        }
    })
        .catch(error => {
        console.error('An error occurred while fetching the post:', error);
    });
}
