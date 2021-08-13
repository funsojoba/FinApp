console.log("Testing static")

const userName = document.querySelector('#username')
const usernameError = document.querySelector('.username-error')
const emailInput = document.querySelector('#your_email')
const emailError = document.querySelector('.email-error')

const passwordInput = document.querySelector("#password")
const passwordError = document.querySelector('.password-error')

const submitBtn = document.querySelector('.register')

const showPassword = document.querySelector('.show')
let toggleShowPassword = false

userName.addEventListener('keyup', (e) => {
    const usernameValue = e.target.value
    userName.classList.remove('invalid')
    usernameError.style.display = 'none'

    if (usernameValue.length > 0) {
        fetch('/auth/validate-username', {
            body: JSON.stringify({ username: usernameValue }),
            method: 'POST'
        }).then(res => res.json())
            .then(data => {
                if (data.username_error) {
                    submitBtn.setAttribute('disabled', 'disabled')
                    usernameError.style.display = 'block'
                    usernameError.innerHTML = data.username_error
                } else {
                    submitBtn.removeAttribute('disabled')
                }
            })
    }
})

emailInput.addEventListener('keyup', (e) => {
    const emailValue = e.target.value
    emailError.style.display = 'none'
    emailInput.classList.remove('invalid')

    if (emailValue.length > 0) {
        fetch('/auth/validate-email', {
            body: JSON.stringify({ email: emailValue }),
            method: 'POST'
        }).then(res => res.json())
            .then(data => {
                if (data.email_error) {
                    submitBtn.disabled = true
                    emailInput.classList.add('invalid')
                    emailError.style.display = 'block'
                    emailError.innerHTML = data.email_error
                } else {
                    submitBtn.disabled = false
                }
            })
    }
})


passwordInput.addEventListener('keyup', (e) => {
    const passwordValue = e.target.value

    passwordInput.classList.remove('invalid')
    passwordError.style.display = 'none'
    if (passwordValue.length < 5) {
        submitBtn.setAttribute('disabled', 'disabled')
        passwordInput.classList.add('invalid')
        passwordError.style.display = 'block'
        passwordError.innerHTML = "password must be more than 5 characters"
    } else {
        submitBtn.removeAttribute('disabled')
    }
})


showPassword.addEventListener('click', () => {
    toggleShowPassword = !toggleShowPassword

    if (toggleShowPassword) {
        showPassword.innerHTML = '<i class="fas fa-eye-slash"></i>'
        passwordInput.setAttribute('type', 'text')
    } else {
        passwordInput.setAttribute('type', 'password')
        showPassword.innerHTML = '<i class="fas fa-eye"></i>'
    }
})