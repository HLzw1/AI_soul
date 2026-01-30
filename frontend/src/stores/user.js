
// 写完后端后，维护登录状态--全局变量，全局变量一般存在stores

import {defineStore} from "pinia";
import {ref} from "vue";

export const useUserStore = defineStore('user', ()=>{
    const id = ref('')
    const username = ref('')
    const photo = ref('')
    const profile = ref('')
    const accessToken = ref('')

    //判断是否登录
    function isLogin(){
        return !!accessToken.value
    }

    //设置accesstoken
    function setAccessToken(token){
        accessToken.value = token
    }

    //保存用户信息
    function setUserInfo(data){
        id.value = data.user_id
        username.value = data.username
        photo.value = data.photo
        profile.value = data.profile
    }

    function logout(){
        id.value = 0
        username.value = ''
        photo.value = ''
        accessToken.value = ''
        profile.value = ''
    }

    return {
        id,
        username,
        photo,
        profile,
        accessToken,
        isLogin,
        setAccessToken,
        setUserInfo,
        logout,
    }
})