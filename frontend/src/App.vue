<script setup>
import NavBar from "@/components/navbar/NavBar.vue";
import {onMounted} from "vue";
import api from "@/js/http/api.js";
import {useUserStore} from "@/stores/user.js";
import {useRoute, useRouter} from "vue-router";

const user = useUserStore()
const route = useRoute();
const router = useRouter(); //可以router到其他页面
//  每次刷新页面，页面挂载调用onMounted，发送get请求（调用后端get_user_info.py），这个请求需要登录
// 第一次请求返回401，然后api封装自动发送refresh_token，云端刷新成功则自动返回一个access_token（情况1） ，被存入user全局状态变量，然后再次发送
// 返回2个401：第一个没有access_token返回401，第二个refresh_token 跨域无法传达返回401
onMounted(async () => {
  try{
    const res = await api.get('/api/user/account/get_user_info/')
    const data = res.data
    if(data.result === 'success'){
      user.setUserInfo(data)
    }
  }catch(err){
  }finally{
    user.setHasPulledUserInfo(true)

    if(route.meta.needLogin && !user.isLogin()){
      await router.replace({
        name: 'user-account-login-index'
      })
    }
  }
})
</script>

<template>
  <NavBar>
    <RouterView />
  </NavBar>
</template>

<style scoped>

</style>
