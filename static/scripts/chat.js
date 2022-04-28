const user_username = JSON.parse(document.getElementById('user_username').textContent)
const roomName = JSON.parse(document.getElementById('room-name').textContent)

const chatSocket = new WebSocket(
    'wss://' +
    window.location.host +
    '/ws/chat/' +
    roomName +
    '/'
);

document.getElementById("chatform").addEventListener("submit", sendMessage)

function sendMessage(e) {
    e.preventDefault()
    const messageInputDom = document.querySelector('#message')
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        "message": message,
        "user": user_username
    }))
    messageInputDom.value = '';
}

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("container", "darker");
    let messageContent = document.createElement("p")
    let usertag = document.createElement("b")
    let username = document.createTextNode(data.user)
    let message = document.createTextNode(data.message)
    messageDiv.appendChild(usertag)
    messageDiv.appendChild(messageContent)
    usertag.appendChild(username)
    messageContent.appendChild(message)
    console.log(messageDiv)
    document.querySelector('#display').appendChild(messageDiv);
}