import { createStore } from 'vuex'
import axios from 'axios'
import Qs from 'qs'

export default createStore({
  state: {
    userInfo: {
      photo: null,
      nickName: null
    }
  },
  mutations: {
    saveUserInfo(state, userInfo) {
      state.userInfo = userInfo;
    }
  },
  actions: {
    tryAutoLogin({commit}, token){
      console.log(token);

      let loginType = false;
      axios({
        method:'post',
        url: "http://127.0.0.1:9000/api-json/userInfo/",
        data: Qs.stringify({
          token,
        })
      }).then((res) => {
        let userInfo = res.data;
        if(userInfo.nickName.length>0) {
          loginType = true;
        }
        commit("saveUserInfo", userInfo)
      })
      return loginType;
    }
  },
  modules: {
  }
})
