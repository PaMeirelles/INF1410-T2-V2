onload = () => {
    const btnRegister = document.getElementById('btnRegister') as HTMLInputElement;
    btnRegister.addEventListener('click', evento => {
        evento.preventDefault();

        const username: string = (document.getElementById('username') as HTMLInputElement).value;
        const email: string = (document.getElementById('email') as HTMLInputElement).value;
        const password: string = (document.getElementById('password') as HTMLInputElement).value;
        const confirmPassword: string = (document.getElementById('confirm_password') as HTMLInputElement).value;
        const msg: HTMLDivElement = document.getElementById('msg') as HTMLDivElement;
        console.log(JSON.stringify({
            'username': username,
            'email': email,
            'password': password
        }))
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
        .then((response: Response) => {
            if (response.ok) {
                return response.json();
            } else if (response.status == 400) {
                msg.innerHTML = 'Usuário ou email já existe.';
            }
            throw new Error('Falha no registro');
        })
        .then((data: { token: string }) => {
            const token: string = data.token;
            window.location.replace('/blog_posts.html');
        })
        .catch(erro => {
            console.log(erro);
        });
    });
};
