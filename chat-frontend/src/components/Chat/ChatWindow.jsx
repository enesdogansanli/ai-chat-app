import React, { useState } from 'react';
import Message from './Message';
import MessageInput from './MessageInput';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = async (messageText) => {
    // Yeni mesajı ekle
    const newMessage = {
      id: Date.now(),
      text: messageText,
      isUser: true
    };
    setMessages([...messages, newMessage]);

    try {
      // Backend'e mesajı gönder
      const response = await fetch('http://localhost:8000/api/chat/message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: messageText }),
      });
      
      const data = await response.json();
      
      // AI yanıtını ekle
      setMessages(msgs => [...msgs, {
        id: Date.now(),
        text: data.response,
        isUser: false
      }]);
    } catch (error) {
      console.error('Mesaj gönderilirken hata:', error);
    }
  };

  return (
    <div className="flex flex-col h-[600px] bg-white rounded-lg shadow">
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message) => (
          <Message
            key={message.id}
            text={message.text}
            isUser={message.isUser}
          />
        ))}
      </div>
      <MessageInput onSendMessage={handleSendMessage} />
    </div>
  );
};

export default ChatWindow;