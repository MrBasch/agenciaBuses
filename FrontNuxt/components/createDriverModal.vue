<template>
  <v-dialog max-width="500px" v-model="open" >
    <v-card class="addDialog">
      <v-card-title class="cardTitle">Add Driver</v-card-title>
      <v-form>
        <v-text-field v-model="name" label="Enter driver name"></v-text-field>
        <v-text-field v-model="rut" label="Enter driver rut"></v-text-field>
        <v-select v-model="state" :items="status" label="Select a state"></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click.stop="saveDriver(name=name,rut=rut,status=state,)" color="#417D7A">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name:'createDriverModal',
  props:['open'],
  data() {
    return {
      name:"",
      rut: "",
      state:'',
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE"]
    };
  },
  methods:{
    async saveDriver(name,rut,status){
        console.log("status", status,"name", name,"rut", rut)
        await fetch(
        `http://127.0.0.1:8000/back/driver?status=${status}&name=${name}&rut=${rut}`,{
            method:"POST",
            mode:'cors',
            headers:{
              "Authorization":`Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea`
            },
            cache:'default'
          }
        ).then((res) => res.json().then(data => console.log(data) ))
      },
    },
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