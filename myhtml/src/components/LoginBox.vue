<template>
  <div id='login-box' v-if="showbox">
    <div id="form">
      <h1>Register</h1>
      <div class="form-item"><input v-model='username' type="text" placeholder="Username"></div>
      <div class="form-item"><input v-model='password' type="text" placeholder="Password"></div>
      <div class="form-item"><button @click='userLogin'>Login</button></div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import swal from 'sweetalert';
  import Qs from 'qs';
  export default{
    name: 'LoginBox',

    data() {
      return{
        username:'',
        password:'',
        showbox: false
      }
    },

    mounted() {
      if(localStorage.getItem('token')){
        this.showbox = false;
      }else{
        this.showbox = true;
      }
    },

    methods:{
      userLogin() {
        // console.log(this.password, this.username);
        axios({
          method:'post',
          url: 'http://127.0.0.1:9000/api-json/login/',
          data: Qs.stringify({
            username: this.username,
            password: this.password,
          })
        }).then((res) => {
          console.log(res.data);
          switch (res.data) {
            case 'user does not exist':
              alert('user does not exist');
              break;
            case 'password error':
              alert('password error');
              break;
          }
          localStorage.setItem('token', res.data);
          swal({
            title: "Successfully",
            content:"successfully login",
            icon: "success",
            buttons: {
              cancel: {
                text: 'cancel',
                value: true,
                visible: false
              },
              confirm: {
                text: 'confirm',
                value: true,
                visible: true
              },
            }
          }).then((isHidden)=> {
            console.log(isHidden);
            if(isHidden) {
              this.showbox = false;
            }
          });
        })
      }
    }
  }
</script>

<style scoped>

#login-box{
  width: 100vw;
  height: 100vh;
  background-color: #00000080;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
#form{
  width: 300px;
  text-align: center;
  background: #979797;
  box-shadow: 0 2px 12px 0 #00000020;
}
#form .form-item{
  margin-top: 10px;
}
#form .form-item button{
  width: 120px;
  height: 30px;
  font-weight: 700;
  font-size: 14px;
  color: white;
  background: skyblue;
  border: none;
  border-radius: 5%;
}
</style>