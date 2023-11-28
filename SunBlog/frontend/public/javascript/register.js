"use strict";
onload = () => {
    const btnRegister = document.getElementById('btnRegister');
    btnRegister.addEventListener('click', evento => {
        evento.preventDefault();
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;
        const msg = document.getElementById('msg');
        console.log(JSON.stringify({
            'username': username,
            'email': email,
            'password': password
        }));
        if (password !== confirmPassword) {
            msg.innerHTML = 'As senhas não coincidem.';
            return;
        }
        fetch(backendAddress + 'accounts/register-api/', {
            method: 'POST',
            body: JSON.stringify({
                'username': username,
                'email': email,
                'password': password
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then((response) => {
            if (response.ok) {
                return response.json();
            }
            else if (response.status == 400) {
                msg.innerHTML = 'Usuário ou email já existe.';
            }
            throw new Error('Falha no registro');
        })
            .then((data) => {
            const token = data.token;
            window.location.replace('/blog_posts.html');
        })
            .catch(erro => {
            console.log(erro);
        });
    });
};
