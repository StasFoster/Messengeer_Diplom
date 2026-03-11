let chat = []

function openModal(id){
    document.getElementById(id).style.display="flex"
}

function closeModal(id){
    document.getElementById(id).style.display="none"
}

window.onclick = function(event){

    document.querySelectorAll(".modal").forEach(modal => {

        if(event.target === modal){
            modal.style.display="none"
        }

    })

}

function addChat(id, username){
    chat.push([id, username])
}

function checkSearch(value, result){
    val = document.getElementById(value)
    res = document.getElementById(result)

    val.addEventListener("input", async function(){
        input = val.value
        if (input.length < 1){
            res.innerHTML = ""
            return
        }
        let response = await fetch(`/api/chats/users/?q=${input}`)
        let list_user = await response.json()
        let users = list_user["users"]
        res.innerHTML = ""
        users.forEach(user => {
            
            let div = document.createElement("div")

            div.innerHTML = `
                ${user.username}
                <button onclick="addChat(user)">Add</button>
            `

            res.appendChild(div)
        })
    })
    }


checkSearch("searchUser1", "result1")
checkSearch("searchUser2", "result2")

