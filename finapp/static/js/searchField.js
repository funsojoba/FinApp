const searchField = document.querySelector("#searchField")
const searchTable = document.querySelector("#table-output")
const appTable = document.querySelector("#app-table")
const pagination = document.querySelector("#pagination")
const searchTableBody = document.querySelector("#search-table-body")



// searchTable.style.display='none'
searchField.addEventListener('keyup', (e)=>{
    searchValue = e.target.value
    if(searchValue.trim().length > 0){
        searchTableBody.innerHTML = ""
        pagination.style.display='none'
        fetch('/search-expense', {
            body:JSON.stringify({searchText:searchValue}),
            method:"POST"
        }).then(res => res.json())
        .then(data =>{
            appTable.style.display = 'none'
            searchTable.style.display ='block'

            if(data.length == 0){
                searchTable.style.display="none"
            }else{
                data.forEach(element => {
                    searchTableBody.innerHTML += `<tr>
                    <td>${element.amount}</td>
                    <td>${element.category}</td>
                    <td>${element.expense_date}</td>
                    <td>${element.description}</td>
                    <td>
                        <a href="edit-expense/${element.id}" class="btn btn-secondary btn-sm"><i class="fas fa-edit"></i> Edit</a>
                    </td>
                </tr>`
                });
            }
        })
    }else{
        searchTable.style.display='none'
        appTable.style.display="block"
        pagination.style.display="block"
    }
})
