const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

document.getElementById('signUpButton').addEventListener('click', () => {
    const email = document.getElementById('signUpEmail').value;
    const emailError = document.getElementById('signUpEmailError');

    if (!validateEmail(email)) {
        emailError.textContent = 'Please use an @ntu.edu.tw email address.';
        emailError.style.color = 'red';
    } else {
        emailError.textContent = '';
        const name = document.getElementById('signUpName').value;
        const password = document.getElementById('signUpPassword').value;

        // Store user data in sessionStorage
        sessionStorage.setItem('user', JSON.stringify({ name, email, password }));
        alert('Sign up successful. Please sign in.');
        container.classList.remove("right-panel-active");
    }
});

document.getElementById('signInButton').addEventListener('click', () => {
    const email = document.getElementById('signInEmail').value;
    const emailError = document.getElementById('signInEmailError');

    if (!validateEmail(email)) {
        emailError.textContent = 'Please use an @ntu.edu.tw email address.';
        emailError.style.color = 'red';
    } else {
        emailError.textContent = '';
        const password = document.getElementById('signInPassword').value;
        const storedUser = JSON.parse(sessionStorage.getItem('user'));

        if (storedUser && storedUser.email === email && storedUser.password === password) {
            alert('Sign in successful');
            // Redirect to account-center.html
            window.location.href = "/account-center";
        } else {
            alert('Invalid email or password');
        }
    }
});

function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@ntu.edu.tw$/;
    return re.test(email);
}

// Check if user is already signed in
document.addEventListener('DOMContentLoaded', () => {
    const storedUser = JSON.parse(sessionStorage.getItem('user'));
    if (storedUser) {
        // Redirect to account-center.html if user is signed in
        window.location.href = "/account-center";
    }
});
