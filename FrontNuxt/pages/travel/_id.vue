<template>
  <p>travel code = {{id}}</p>
</template>

<script>
export default {
    head(){
        return{
            title: `travel ${this.id}`
        }  
    },
    data(){
        return{
            id:this.$route.params.id,
        }
    },
}
</script>

<style>

</style>