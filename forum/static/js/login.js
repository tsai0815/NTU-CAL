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

        fetch('/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: `signup=true&username=${encodeURIComponent(name)}&email=${encodeURIComponent(email)}&password1=${encodeURIComponent(password)}&password2=${encodeURIComponent(password)}`
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Sign up successful. Please sign in.');
                    container.classList.remove("right-panel-active");
                } else {
                    const errors = JSON.parse(data.errors);
                    let errorMessage = 'Sign up failed:';
                    for (const field in errors) {
                        errorMessage += `\n${field}: ${errors[field].map(error => error.message).join(', ')}`;
                    }
                    alert(errorMessage);
                }
            })
            .catch(error => console.error('Error:', error));
    }
});

document.getElementById('signInButton').addEventListener('click', () => {
    const email = document.getElementById('signInEmail').value;
    const emailError = document.getElementById('signInEmailError');
    const next = document.getElementById('next').value;

    if (!validateEmail(email)) {
        emailError.textContent = 'Please use an @ntu.edu.tw email address.';
        emailError.style.color = 'red';
    } else {
        emailError.textContent = '';
        const password = document.getElementById('signInPassword').value;

        fetch('/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: `signin=true&email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}&next=${encodeURIComponent(next)}`
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Sign in successful');
                    window.location.href = next || "/account-center";
                } else {
                    const errors = JSON.parse(data.errors);
                    let errorMessage = 'Sign in failed:';
                    for (const field in errors) {
                        errorMessage += `\n${field}: ${errors[field].map(error => error.message).join(', ')}`;
                    }
                    alert(errorMessage);
                }
            })
            .catch(error => console.error('Error:', error));
    }
});

function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@ntu.edu.tw$/;
    return re.test(email);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
