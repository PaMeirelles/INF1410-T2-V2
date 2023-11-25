onload = (evento) => {
    (document.getElementById('logout') as HTMLInputElement).addEventListener('click', (evento) => {
        const token = localStorage.getItem('token');
        fetch(backendAddress + 'accounts/token-auth/', {
            method: 'DELETE',
            headers: getHeaders()
        })
        .then(response => {
            const mensagem = document.getElementById('mensagem') as HTMLDivElement;
            if(response.ok) window.location.assign('/');
            else mensagem.innerHTML = 'Erro ' + response.status;
        })
        .catch(erro => { 
            console.log(erro); 
        })
    });
}

function getHeaders() {
    const token = localStorage.getItem('token');
    return {
        'Authorization': 'Token ' + token,
        'Content-Type': 'application/json'
    };
}