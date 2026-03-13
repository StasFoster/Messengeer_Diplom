let chat = {}



function openModal(id){
    document.getElementById(id).style.display="flex"
}

function closeModal(id){
    document.getElementById(id).style.display="none"
}

function addChat(id, username, members){
    let mem = document.getElementById(members)
    if(id in chat){
        console.log("есть в чате")
    }
    else{
        chat[id] = username
        let div = document.createElement("div")
        div.className = "el_search_chat"
        div.innerHTML = `
            <p>${username}</p>
        `
        mem.appendChild(div)
    }
}

window.onclick = function(event){

    document.querySelectorAll(".modal").forEach(modal => {

        if(event.target === modal){
            modal.style.display="none"
        }

    })

}

function checkSearch(value, result,members, mode=0){
    let val = document.getElementById(value)
    let res = document.getElementById(result)
    
    
    val.addEventListener("input", async function(){
        text = val.value
        
        if (text.length < 1){
            res.innerHTML = ""
            console.log(val.value)
            return
        }
        let response = await fetch(`/api/chats/users/?q=${text}`)
        let list_user = await response.json()
        let users = list_user["users"]
        res.innerHTML = ""
        console.log(users)
        users.forEach(user => {
            
            let div = document.createElement("div")
            div.className = "el_search_chat"
            switch (mode) {
                case 1:
                     div.innerHTML = `
                        ${user.username}
                        <button type="button" onclick="addChat(${user.id}, '${user.username}','${members}')">Add</button>
                    `  
                    break;
                
                case 0:
                     div.innerHTML = `
                        ${user.username}
                        <button type="button" onclick="addDialog()">Add</button>
                    `  
                    break;
            
                default:
                    break;
            }
            
            res.appendChild(div)
        })
    })
}

document.addEventListener('DOMContentLoaded', function() {
    checkSearch("searchUser1", "result1", "members", 1)
    checkSearch("searchUser2", "result2", "members2")
});