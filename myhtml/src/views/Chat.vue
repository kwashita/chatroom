<template>
  <div id="page-box">
    <img src="http://127.0.0.1:9000/upload/image1.jpg" alt="" />
    <h1>chat room</h1>
    <div class="message-list">
      <div class="message" v-for="(item, index) in msgList" :key="index">
        {{item}}
      </div>
    </div>
    <div id="userinfo">
      <img :src="userInfo.photo" alt="">
      <span> {{userInfo.nickName}} : </span>
    </div>
    <div class="text-input">
      <textarea v-model='text_input' name="" id="" cols="30" rows="10" ></textarea>
      <button @click='clickSendMessage'>Send</button>
    </div>
    <LoginBox></LoginBox>
    <router-view></router-view>
  </div>
</template>
<script>
import axios from "axios";
import Loginbox from '../components/LoginBox'
// import store from '../store'
export default {
  data() {
    return {
      text: '',
      text_input: '',
      msgList: [],
      //vuex userinfo
    };
  },

  components:{
    'LoginBox': Loginbox
  },
  computed: {
    userInfo(){
      return this.$store.state.userInfo
    }
  },
  // beforeRouteEnter(to,from,next){
  //   // this.autoLogin();
   
  // },
  mounted() {
    this.autoLogin();
    this.getData();
    this.initWebSocket();
  },

  methods: {
    autoLogin() {
      // let userInfo = {
      //   photo: "http://127.0.0.1:9000/upload/image1.jpg",
      //   nickName: "hahaha"
      // }
      // this.$store.commit("saveUserInfo", userInfo);
      this.$store.dispatch("tryAutoLogin", localStorage.getItem('token'));
    },

    clickSendMessage() {

      // this.msgList.push(this.text_input);
      let msg = {
        code: 200,
        message: this.text_input
      }
      this.sendMessage(msg);
    },

    //retreive data
    getData() {
      axios({
        method: "get",
        url: "http://127.0.0.1:9000/api/",
      }).then((res) => {
        this.text = res.data.test;
      });
    },

    //initial websocket
    initWebSocket() {
      this.websocket = new WebSocket('ws://127.0.0.1:9000/chat/myroom/');
      console.log(this.websocket);
      this.websocket.onopen = this.onOpen;
      this.websocket.onmessage = this.onMessage;
      this.websocket.onclose = this.onClose;
      this.websocket.onerror = this.onError;
    },

    sendMessage(msg) {
      let text_data = JSON.stringify(msg);
      this.websocket.send(text_data);
    },

    onOpen(r) {
      console.log('connect opened');
      console.log(r);

      let msg = {
        //100 means user is coming
        code: 100,
        message: 'Join the room'
      }
      this.sendMessage(msg);
    },

    onMessage(r) {
      let message = JSON.parse(r.data).message;
      console.log(message);
      this.msgList.push(message)
    },

    onClose() {

    },

    onError() {

    },

  },
};
</script>
<style>
* {
  margin: 0;
  padding: 0;
}
#page-box {
  width: 300px;
  height: 600px;
  box-shadow: 0 2px 12px 0 #000;
  color: red;
  margin: 0 auto;
}
#page-box img {
  width: 100%;
}
.message-list{
  height: 300px;
  overflow-y: scroll;
}
.message {
  width:40%;
  /* height: 20px; */
  margin-top: 5px;
  background: skyblue;
  word-break: break-all;
  word-wrap: break-word;
}
.text-input{
  display: flex;
  justify-content: space-between;
}
.text-input textarea{
  width: 70%;
  height: 100px;

}
.text-input  button{
  width: 75px;
  height: 60px;
  background-color: yellow;
}
#userinfo{
  display: flex;
  align-items: center;
}
#userinfo img{
  width: 30px;
}
</style>
