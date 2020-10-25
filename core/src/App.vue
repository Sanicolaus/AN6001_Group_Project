<template>
  <div :style="{ background: backgroundColor }" id="app">
    <beautiful-chat
      :alwaysScrollToBottom="alwaysScrollToBottom"
      :close="() => {}"
      :colors="colors"
      :isOpen="true"
      :messageList="messageList"
      :messageStyling="messageStyling"
      :newMessagesCount="newMessagesCount"
      :sendMessage="sendMessage"
      :onMessageWasSent="onMessageWasSent"
      :open="() => {}"
      :participants="participants"
      :showCloseButton="false"
      :showLauncher="false"
      :showEmoji="true"
      :showFile="true"
      :showTypingIndicator="showTypingIndicator"
      :showEdition="true"
      :showDeletion="true"
      :showConfirmationDeletion="true"
      :confirmationDeletionMessage="'Are you sure to delete this?'"
      :titleImageUrl="titleImageUrl"
      @onType="handleOnType"
      @edit="editMessage"
      @remove="removeMessage"
    >
      <template v-slot:header>
        <h2>AI Diagnose Bot</h2>
      </template>
    </beautiful-chat>
  </div>
</template>

<script>
import messageHistory from "./messageHistory";
import chatParticipants from "./chatProfiles";
import availableColors from "./colors";
import axios from "axios";

export default {
  name: "app",
  data() {
    return {
      participants: chatParticipants,
      titleImageUrl:
        "https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png",
      // messageList: messageHistory,
      messageList: [
        { type: "text", author: `bot`, id: 0, data: { text: `Hello` } },
      ],
      newMessagesCount: 0,
      isChatOpen: true,
      showTypingIndicator: "",
      colors: null,
      availableColors,
      chosenColor: null,
      alwaysScrollToBottom: true,
      messageStyling: true,
      userIsTyping: false,
    };
  },
  created() {
    this.setColor("blue");
  },
  methods: {
    sendMessage(text) {
      if (text.length > 0) {
        this.onMessageWasSent({
          author: "me",
          type: "text",
          id: Math.random(),
          data: { text },
        });
      }
    },
    handleTyping(text) {
      this.showTypingIndicator =
        text.length > 0
          ? this.participants[this.participants.length - 1].id
          : "";
    },
    async getResponse(question) {
      try {
        let response = await axios.get(`http://localhost:5000/asked/${question}`)
        console.log(response.data)
        this.messageList=[
          ...this.messageList, 
          {
            author: "bot",
            type: "text",
            id: Math.random(),
            data: {text: response.data.questions},
            suggestions: response.data.suggestions == null ? [] : response.data.suggestions
          },
        ]
      }catch(err){console.warn(err)}
    },
    onMessageWasSent(message) {
      this.messageList = [
        ...this.messageList,
        Object.assign({}, message, { id: Math.random() }),
      ];
      let responseText = "Got it";
      this.getResponse(message.data.text);
    },
    setColor(color) {
      this.colors = this.availableColors[color];
      this.chosenColor = color;
    },
    showStylingInfo() {
      this.$modal.show("dialog", {
        title: "Info",
        text:
          "You can use *word* to <strong>boldify</strong>, /word/ to <em>emphasize</em>, _word_ to <u>underline</u>, `code` to <code>write = code;</code>, ~this~ to <del>delete</del> and ^sup^ or ¡sub¡ to write <sup>sup</sup> and <sub>sub</sub>",
      });
    },
    messageStylingToggled(e) {
      this.messageStyling = e.target.checked;
    },
    handleOnType() {
      this.$root.$emit("onType");
      this.userIsTyping = true;
    },
    editMessage(message) {
      const m = this.messageList.find((m) => m.id === message.id);
      m.isEdited = true;
      m.data.text = message.data.text;
    },
    removeMessage(message) {
      const m = this.messageList.find((m) => m.id === message.id);
      m.type = "system";
      m.data.text = "This message has been removed";
    },
    like(id) {
      const m = this.messageList.findIndex((m) => m.id === id);
      var msg = this.messageList[m];
      msg.liked = !msg.liked;
      this.$set(this.messageList, m, msg);
    },
  },
  computed: {
    linkColor() {
      return this.chosenColor === "dark"
        ? this.colors.sentMessage.text
        : this.colors.launcher.bg;
    },
    backgroundColor() {
      return this.chosenColor === "dark" ? this.colors.messageList.bg : "#fff";
    },
  },
  mounted() {
    this.messageList.forEach((x) => (x.liked = false));
  },
};
</script>

<style>
body {
  padding: 0px;
  margin: 0px;
}

* {
  font-family: Avenir Next, Helvetica Neue, Helvetica, sans-serif;
}
</style>
