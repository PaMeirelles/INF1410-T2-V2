onload = function(){exibeDetalhes();}

function exibeDetalhes() {
    const urlParams = new URLSearchParams(window.location.search);
    const postId = urlParams.get('id');
    const token = localStorage.getItem('token');
    fetch(backendAddress + "api/getumpost/" + postId, {
        method: 'GET',
        headers: {
        'Authorization': 'token ' + token
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(response => {
            console.log(response)
            const postElement = document.getElementById('post-detail');
            let userId = response.user_id
            let post = response.posts
            console.log(userId);
            console.log(post.autor);
            if (postElement) {
                let html = `
                    <h1>${post.titulo}</h1>
                    <p>${post.corpo}</p>
                    <p>Publicado em ${post.dt_publicado} por ${post.autor}</p>
                    <a href="blog_posts.html">Voltar para a lista de posts</a>
                `;
                if (post.autor == userId) {
                    html += `<a href="edit_post.html?id=${post.id}">Editar este post</a>`;
                }
                postElement.innerHTML = html;
            } else {
                console.error('Element with id "post-detail" not found');
            }
        })
        .catch(error => {
            console.error('An error occurred while fetching the post:', error);
        });
}