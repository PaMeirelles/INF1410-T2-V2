const loginPageUrl = 'login.html';
const logoutPageUrl = 'logout.html';
const registerPageUrl = 'register.html';
const newPostUrl = 'new_blog.html'

document.addEventListener('DOMContentLoaded', () => {
  const userStatusContainer = document.getElementById('userStatus');

  // Check if the user is authenticated (you can use your own logic, e.g., checking for a token in local storage)
  const isAuthenticated = localStorage.getItem('token') !== null;

  if (isAuthenticated) {
    const username = localStorage.getItem('username') || 'Guest';

    // Display "logged as xxxx" and a logout button
    userStatusContainer.innerHTML = `Logged as ${username} | <a href="${logoutPageUrl}">Logout</a> | <a href="${newPostUrl}">Criar Postagem</a>`;
  } else {
    // Display login and register links
    userStatusContainer.innerHTML = `<a href="${loginPageUrl}">Login</a> | <a href="${registerPageUrl}">Register</a>`;
  }
});
