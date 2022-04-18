<template>
  <v-dialog max-width="500px" v-model="open" >
    <v-card class="addDialog">
      <v-card-title>Add Bus</v-card-title>
      <v-form>
        <v-text-field v-model="code" label="Enter bus code"></v-text-field>
        <v-select v-model="state" :items="status" label="Select A Status"></v-select>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click.stop="saveBus(code=code,status=state)" color="green">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name:'busModal',
  props:['open'],
  data() {
    return {
      code:"",
      state: "",
      title: "",
      author: "",
      description: "",
      status: ["AVAILABLE", "ON_THE_WAY", "UNAVAILABLE","ON_REPAIR"]
    };
  },
  methods:{
    async saveBus(code,status){
        console.log("code =", code, "status = ", status)
        await fetch(
        `http://127.0.0.1:8000/back/bus?code=${code}&status=${status}`,{
            method:"POST",
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
</style>