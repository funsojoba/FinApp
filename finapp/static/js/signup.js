console.log("Testing static")

const userName = document.querySelector('#username')
const usernameError = document.querySelector('.username-error')

userName.addEventListener('keyup', (e)=>{
    const usernameValue = e.target.value


    userName.classList.remove('invalid')
    usernameError.style.display = 'none'

    if(usernameValue.length > 0){
        fetch('/auth/validate-username',{
            body: JSON.stringify({ username: usernameValue }),
            method:'POST'
        }).then(res => res.json())
        .then(data =>{
            console.log(data)
            if(data.username_error){
                userName.classList.add('invalid')
                usernameError.style.display='block'
                usernameError.innerHTML = data.username_error
            }
        })
    }
})