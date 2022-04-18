<template>
  <h1>{{msg}}</h1>
</template>

<script>
export default {
    data(){
        return{
            msg:'',
        }
    },
    methods:{
        async createData(){
            await fetch(
            `http://127.0.0.1:8000/back/create_data`,{
                method:"GET",
                mode:'cors',
                headers:{
                "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
                },
                cache:'default'
            }
            ).then((res) => res.json().then(data => this.msg=data))
        },
    },
    created(){
        this.createData()
    }
}
</script>

<style>

</style>