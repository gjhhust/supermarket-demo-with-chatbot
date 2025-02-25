/* static/chatbot/js/chatbot.js */

document.addEventListener('DOMContentLoaded', function() {
    const floatButton = document.getElementById('chatbot-float-button');
    const chatbotWidget = document.getElementById('chatbot-widget');
    const closeButton = document.getElementById('chatbot-close-button');
    const sendButton = document.getElementById('chatbot-send-button');
    const inputField = document.getElementById('chatbot-input');
    const messagesDiv = document.getElementById('chatbot-messages');

    // 点击浮标展开/收起聊天窗口
    floatButton.addEventListener('click', function() {
        chatbotWidget.style.display = chatbotWidget.style.display === 'none' ? 'flex' : 'none';
    });

    closeButton.addEventListener('click', function() {
        chatbotWidget.style.display = 'none';
    });

    sendButton.addEventListener('click', sendMessage);

    inputField.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const query = inputField.value.trim();
        if (query) {
            appendMessage('user', query); // 显示用户消息
            inputField.value = ''; // 清空输入框

            // 发送消息到 Django 后端 API (需要配置正确的 URL)
            fetch('/chatbot/api/response/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken'), // 获取 CSRF token
                },
                body: 'query=' + encodeURIComponent(query)
            })
            .then(response => response.json())
            .then(data => {
                if (data.reply) {
                    appendMessage('bot', data.reply); // 显示机器人回复
                } else if (data.error) {
                    appendMessage('bot', 'Error: ' + data.error); // 显示错误信息
                }
            })
            .catch(error => {
                appendMessage('bot', 'Error: Network error. Please try again.');
            });
        }
    }

    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('chatbot-message');
        messageDiv.classList.add(sender);

        const messageContent = document.createElement('p');
        messageContent.textContent = message;
        messageDiv.appendChild(messageContent);

        messagesDiv.appendChild(messageDiv);
        messagesDiv.scrollTop = messagesDiv.scrollHeight; // 滚动到底部
    }

    // 获取 CSRF Token (用于 Django CSRF 保护)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});