<template>
  <v-dialog max-width="500px" v-model="edit" >
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Update or create City</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter city name"></v-text-field>
        <v-text-field v-model="code" label="Enter city code"></v-text-field>
        <v-text-field v-model="new_code" label="Enter city new_code"></v-text-field>
        
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click.stop="updateCity(name=name,code=code,new_code=new_code)" color="#417D7A">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name:'updateBusModal',
  props:['edit'],
  data() {
    return {
      code:"",
      state: "",
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE","ON_REPAIR"]
    };
  },
  methods:{
    async updateCity(name,code,new_code){
        await fetch(
        `http://127.0.0.1:8000/back/city?code=${code}&name=${name}&new_code=${new_code}`,{
            method:"PUT",
            mode:'cors',
            headers:{
              "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
            },
            cache:'default'
          }
        ).then((res) => res.json().then(data => console.log(data) ))
      },
  }
}
</script>
<style scoped>
.addDialog{
  overflow: hidden;
  background-color: #8b8070;
}
.cardTitle{
    background-color: #1A3C40;
}
</style>