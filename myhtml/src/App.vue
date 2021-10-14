<template>
  <div id="page-box">
    <img src="http://127.0.0.1:9000/upload/image1.jpg" alt="" />
    <h1>123123</h1>
  </div>
</template>
<script>
import axios from "axios";
export default {
  date() {
    return {
      text: "",
    };
  },

  mounted() {
    this.getData();
  },

  methods: {
    //retreive data
    getData() {
      axios({
        method: "get",
        url: "http://127.0.0.1:9000/api/",
      }).then((res) => {
        console.log(res);
      });
    },
  },
};
</script>
<style>
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
</style>
