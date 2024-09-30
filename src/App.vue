<template>
  
  <div class="chat-container">
    <div v-for="(message, index) in messages" :key="index" class="message">
      <div v-if="message.type === 'user'" class='message-user' >
        <b> (User) </b>
        <font-awesome-icon icon="user" />
        <b> : </b> 
        {{ message.text }}
      </div>
      <div v-else-if="message.type === 'bot'" class='message-bot'>
        <b> (Bot) </b>
        <font-awesome-icon icon="robot" />
        <b> : </b> {{ message.text }}
      </div>
    </div>
    <div class="chat-input">
      <input type="text" placeholder="Enter Your message" v-model="newMessage" @input="adjustInputWidth">
      <div class="button">
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'App',
  data() {
    return {
      messages: [],
      newMessage: '',
      maxDisplayedMessages: 10
    };
  },
  computed: {
    displayedMessages() {
      return this.messages.slice(0, this.maxDisplayedMessages);
    }
  },
  methods: {
    adjustInputWidth(event) {
      const input = event.target;
      input.style.width = `${input.value.length + 1}ch`;
    },
    async sendMessage()
    {
      if (this.newMessage.trim() !== '') {
        this.messages.push({ type: 'user', text: this.newMessage });
        try
        {
          await axios.post('http://127.0.0.1:5000/message_input', { text: this.newMessage});
          const response = await axios.get('http://127.0.0.1:5000/message_input')
          this.messages.push({type: 'bot', text: response.data.response})
          while (this.messages.length > this.maxDisplayedMessages) { // remove the messages
            this.messages.shift(); // Remove the oldest message
            }
        }
        catch(error)
        {
          console.error(error);
        }
        this.newMessage = '';
      }
     
     
    }
  },
  mounted() {
    // Any initialization code can go here
  }
};
</script>

<style scoped>

/* Global styles */
.chat-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    width: 110vh; /* Increase width to 80% of the parent container */
    height: 85vh; /* Increase height to 80% of the viewport height */
    border-color: aqua;
    margin: 0 auto;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 20px; /* Increase padding for more space inside the container */
    background-color: #5e6061;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
.chat-input {
    display: flex;
    justify-content: space-between;
}
.chat-input input {
    width: 70%; /* Adjust width as needed */
    height: 40px; /* Adjust height as needed */
    padding: 10px;
    border-radius: 1px;
    border: 1px solid #ccc;
}
.chat-input :hover
{
  box-shadow: 0 4px 8px rgba(0, 1, 0.1, 0.1); /* Slightly stronger shadow */
  animation: pulse 2s infinite;
}
.button button {
    width: 100px; /* Adjust width as needed */
    height: 40px; /* Adjust height as needed */
    border-radius: 5px;
    border: none;
    background-color: #161716;
    color: white;
    cursor: pointer; /* set up the cursor */
}
.button button:hover {
    background-color: #0c6848;
    animation: shake 1s infinite;
}
.message {
    border: 2px solid #1e211e; /* Green border */
    padding: 10px;
    border-radius: 10px; /* More rounded corners */
    background: linear-gradient(135deg, #5e6061 25%, #7a7c7d 100%); /* Gradient background with similar colors */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Font style */
    color: #ffffff; /* White text color for contrast */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Slightly stronger shadow */
    animation: pulse 2s infinite; /* Animation effect */
    margin-top: 10px;
}
.message :hover
{
  box-shadow: 0 4px 8px rgba(0, 1, 0.1, 0.1); /* Slightly stronger shadow */
  animation: shake 2s infinite;
}
.message-bot {
  font-family: 'VT323', monospace;
  color: #c1b153; /* Gold text color for bot messages */

}
.message-user {
  font-family: 'Audiowide', cursive;
  color: #071607; /* Lime text color for user messages */

  
}
@keyframes pulse {
    0% {
        transform: scale(1);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    50% {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    100% {
        transform: scale(1);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
}



/*
  define the animation frame called 
*/
@keyframes shake {
  from {
    transform: translateX(5%);
    transform: translateY(5%);

  }
  to {
    transform: translateY(10%);
    transform: translateX(10%);

  }
}

</style>
