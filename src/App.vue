<template>
  <div class="chat-container">
    <div v-for="(message, index) in messages" :key="index" class="message">
      <div>
        <font-awesome-icon icon="user" />
        <b> : </b>
      </div>
      {{ message }}
  
    </div>
    
    <div class = "chat-input">
      <input type = "text" placeholder="enter words" v-model="newMessage" @input="adjustInputWidth" >
      <div class = "button">
        <button @click="sendMessage">Send</button>
      </div>
    </div>
    
    <div>

    </div>
    </div>
</template>

<script>

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
    displayedMessages()
    {
      return this.messages.slice(0, this.maxDisplayedMessages);
    }
  },

  methods: {
    adjustInputWidth(event) {
      const input = event.target;
      input.style.width = `${input.value.length + 1}ch`;
    },
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.unshift(this.newMessage);
        this.newMessage = '';
        if (this.messages.length > this.maxDisplayedMessages) {
          this.messages.pop(); // Remove the oldest message
        }
        this.newMessage = '';
      }
    }
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
    height: 80vh; /* Increase height to 80% of the viewport height */
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
    border-radius: 5px;
    border: 1px solid #ccc;

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
    background-color: #e6eaef;
}
.message
{
  display: flex;
  justify-content: space-between;
  color:#161716;
  margin-bottom: 10px; /* Add some space between messages */
  font-size: large;
  font-family: 'Times New Roman', Times, serif;
  color: 000000;
  max-height: 100px; /* Limit the height of each message */
  overflow: hidden; /* Hide overflow content */
  text-overflow: ellipsis; /* Add ellipsis for overflow text */
  border: 1px solid cadetblue;
  animation: 0.5s linear 1s infinite running shake;
}

/*
  define the animation frame called 
*/
@keyframes shake {
  from {
    transform: translateY(10%);
  }
  to {
    transform: translateY(0);
  }
}

</style>
