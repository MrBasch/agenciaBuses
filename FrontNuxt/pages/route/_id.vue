<template>
  <div class="header_">
          <h1>Route id : {{id}}</h1>
        </div>
</template>

<script>
export default {
    head(){
        return{
            title: `Route ${this.id}`
        }  
    },
    data(){
        return{
            id:this.$route.params.id,
        }
    },
    methods:{
        async getRouteByID(id) {
            await fetch(
            'http://127.0.0.1:8000/back/route',{
                method:"GET",
                mode:'cors',
                headers:{
                "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
                },
                cache:'default'
            }
            ).then((res) => res.json().then(data=> {
                console.log("data =", data)
                return this.routes = data
            }))
        },
    }
}
</script>

<style>

</style>